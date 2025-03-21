from datetime import date, datetime
import pytest
import numpy as np
from uuid import uuid4
from faker import Faker
from typing import List

from src.commons.lending import LendingEvents

fake = Faker("pt_BR")


class TestLendingEvents:
    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (100, 100),
        ],
        ids=[
            "generate_five_loans",
            "generate_zero_loans",
            "generate_one_loan",
            "generate_many_loans",
        ],
    )
    def test_generate_loans(self, count: int, expected_length: int):

        loans = LendingEvents.generate_loans(count)

        assert len(loans) == expected_length
        if loans:
            for loan in loans:
                assert isinstance(loan["loan_id"], str)
                assert isinstance(loan["user_id"], str)
                assert 1000 <= loan["amount"] < 50000
                assert 2.5 <= loan["interest_rate"] <= 15.0
                assert 12 <= loan["term"] <= 60
                assert isinstance(loan["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (50, 50),
        ],
        ids=[
            "generate_five_payments",
            "generate_zero_payments",
            "generate_one_payment",
            "generate_many_payments",
        ],
    )
    def test_generate_payments(self, count: int, expected_length: int):

        payments = LendingEvents.generate_payments(count)

        assert len(payments) == expected_length
        if payments:
            for payment in payments:
                assert isinstance(payment["payment_id"], str)
                assert isinstance(payment["loan_id"], str)
                assert 100 <= payment["amount"] < 2000
                assert isinstance(payment["date"], (str, date, datetime))
                assert payment["status"] in ["completed", "pending", "failed"]
                assert isinstance(payment["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (3, 3),
            (0, 0),
            (1, 1),
            (75, 75),
        ],
        ids=[
            "generate_three_credit_scores",
            "generate_zero_credit_scores",
            "generate_one_credit_score",
            "generate_many_credit_scores",
        ],
    )
    def test_generate_credit_score(self, count: int, expected_length: int):

        credit_scores = LendingEvents.generate_credit_score(count)

        assert len(credit_scores) == expected_length
        if credit_scores:
            for credit_score in credit_scores:
                assert isinstance(credit_score["score_id"], str)
                assert isinstance(credit_score["user_id"], str)
                assert 1 <= credit_score["score"] <= 1000
                assert isinstance(credit_score["last_updated"], (str, date, datetime))
                assert isinstance(credit_score["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (2, 2),
            (0, 0),
            (1, 1),
            (25, 25),
        ],
        ids=[
            "generate_two_risk_assessments",
            "generate_zero_risk_assessments",
            "generate_one_risk_assessment",
            "generate_many_risk_assessments",
        ],
    )
    def test_generate_risk_assessment(self, count, expected_length):

        risk_assessments = LendingEvents.generate_risk_assessment(count)

        assert len(risk_assessments) == expected_length
        if risk_assessments:
            for risk_assessment in risk_assessments:
                assert isinstance(risk_assessment["assessment_id"], str)
                assert isinstance(risk_assessment["user_id"], str)
                assert risk_assessment["risk_level"] in ["low", "medium", "high"]
                assert isinstance(risk_assessment["details"], str)
                assert isinstance(risk_assessment["date"], (str, date, datetime))
                assert isinstance(risk_assessment["created_at"], (str, date, datetime))
