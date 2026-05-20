import unittest
from pathlib import Path
import os

from fastapi.testclient import TestClient

TEST_DB_PATH = Path(__file__).resolve().parent / "lexindia_test_runtime.db"
if TEST_DB_PATH.exists():
    TEST_DB_PATH.unlink()

os.environ["APP_ENV"] = "test"
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB_PATH.as_posix()}"
os.environ["DATABASE_FALLBACK_URL"] = f"sqlite:///{TEST_DB_PATH.as_posix()}"
os.environ["ENABLE_DB_FALLBACK"] = "false"
os.environ["TEST_DATABASE_URL"] = f"sqlite:///{TEST_DB_PATH.as_posix()}"
os.environ["AUTH_JWT_SECRET"] = "test-suite-secret"
os.environ["CORS_ALLOWED_ORIGINS"] = "http://127.0.0.1:3000"
os.environ["BOOTSTRAP_MODE"] = "true"
os.environ["BOOTSTRAP_DEMO_DATA"] = "true"
os.environ["BOOTSTRAP_ADMIN_EMAIL"] = "admin.test@lexindia.in"
os.environ["BOOTSTRAP_ADMIN_PASSWORD"] = "LexIndiaTest123"
os.environ["BOOTSTRAP_ADMIN_NAME"] = "LexIndia Test Admin"

from db.postgres import reset_database_state
import main

reset_database_state()


class LexIndiaApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client_context = TestClient(main.app)
        cls.client = cls.client_context.__enter__()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client_context.__exit__(None, None, None)
        reset_database_state()
        if TEST_DB_PATH.exists():
            TEST_DB_PATH.unlink()

    def test_health_endpoint(self) -> None:
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_research_search_returns_demo_fallback(self) -> None:
        response = self.client.get(
            "/api/v1/research/search",
            params={"query": "ipc 302 bns", "limit": 3},
        )
        payload = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(payload["count"], 1)
        self.assertEqual(payload["meta"]["mode"], "hybrid-with-demo-fallback")

    def test_research_analysis_returns_structured_payload(self) -> None:
        response = self.client.post(
            "/api/v1/research/analyze",
            json={"scenario": "How should a government portal respond to a privacy breach complaint?"},
        )
        payload = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("analysis", payload)
        self.assertIn("structured_response", payload)
        self.assertIn("risk_level", payload["analysis"])

    def test_document_compare_flags_amount_delta(self) -> None:
        response = self.client.post(
            "/api/v1/documents/compare",
            json={
                "document_a": "The liability cap is INR 500000 and the response time is 48 hours.",
                "document_b": "The liability cap is INR 250000 and the response time is 72 hours.",
            },
        )
        payload = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(payload["contradictions"]), 1)

    def test_auth_register_login_and_me(self) -> None:
        register_response = self.client.post(
            "/api/v1/auth/register",
            json={
                "email": "owner.lexindia@example.com",
                "password": "PitchReady123",
                "full_name": "Owner LexIndia",
                "role": "admin",
            },
        )
        self.assertEqual(register_response.status_code, 201)

        login_response = self.client.post(
            "/api/v1/auth/login",
            json={
                "email": "owner.lexindia@example.com",
                "password": "PitchReady123",
            },
        )
        self.assertEqual(login_response.status_code, 200)
        token = login_response.json()["access_token"]

        me_response = self.client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {token}"},
        )
        self.assertEqual(me_response.status_code, 200)
        self.assertEqual(me_response.json()["email"], "owner.lexindia@example.com")

    def test_workflow_persistence(self) -> None:
        login_response = self.client.post(
            "/api/v1/auth/login",
            json={
                "email": "admin.test@lexindia.in",
                "password": "LexIndiaTest123",
            },
        )
        self.assertEqual(login_response.status_code, 200)
        token = login_response.json()["access_token"]
        auth_header = {"Authorization": f"Bearer {token}"}

        create_response = self.client.post(
            "/api/v1/workflow/",
            json={
                "template_id": "wf-research-memo",
                "name": "Cabinet note support",
                "matter": "Policy note review",
                "status": "active",
                "priority": "high",
                "summary": "Prepare a statutory and privacy risk brief.",
                "next_action": "Assign counsel and delivery owner.",
                "metadata": {"department": "Digital governance"},
            },
            headers=auth_header,
        )
        self.assertEqual(create_response.status_code, 201)
        workflow_id = create_response.json()["id"]

        update_response = self.client.patch(
            f"/api/v1/workflow/{workflow_id}",
            json={"status": "review", "next_action": "Prepare final briefing for secretary."},
            headers=auth_header,
        )
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.json()["status"], "review")

        list_response = self.client.get("/api/v1/workflow/", headers=auth_header)
        self.assertEqual(list_response.status_code, 200)
        self.assertTrue(any(item["id"] == workflow_id for item in list_response.json()["workflows"]))


if __name__ == "__main__":
    unittest.main()
