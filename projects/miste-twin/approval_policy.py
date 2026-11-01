"""Central authority rules for local and external actions."""

from __future__ import annotations


class ApprovalPolicy:
    AUTONOMOUS_LOCAL_ACTIONS = {
        "research",
        "analysis",
        "prioritize",
        "dashboard.create",
        "dashboard.update",
        "dashboard.complete",
        "dashboard.archive",
        "dashboard.remove",
        "dashboard.restore",
        "draft",
        "classify",
        "schedule.local",
        "briefing",
    }

    APPROVAL_REQUIRED = {
        "substantive_reply",
        "send_message",
        "send_connection_request",
        "submit_job_application",
        "publish_post",
        "schedule_interview",
        "salary_decision",
        "accept_project",
        "accept_collaboration",
        "legal_commitment",
        "financial_commitment",
        "upload_document",
        "create_obligation",
    }

    def requires_approval(self, action_type: str) -> bool:
        return action_type in self.APPROVAL_REQUIRED

    def permits_autonomous(self, action_type: str) -> bool:
        return action_type in self.AUTONOMOUS_LOCAL_ACTIONS

    def authorize(self, action_type: str, approved: bool = False) -> dict[str, object]:
        if self.requires_approval(action_type):
            return {
                "allowed": bool(approved),
                "requires_approval": True,
                "external_action": action_type,
            }
        return {
            "allowed": self.permits_autonomous(action_type),
            "requires_approval": False,
            "external_action": None,
        }
