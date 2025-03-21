from datetime import date, datetime
import pytest
from faker import Faker

from commons.insurance import InsuranceEvents

fake = Faker("pt_BR")


class TestInsuranceEvents:
    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (100, 100),
        ],
        ids=[
            "generate_five_policies",
            "generate_zero_policies",
            "generate_one_policy",
            "generate_many_policies",
        ],
    )
    def test_generate_policies(self, count: int, expected_length: int):

        policies = InsuranceEvents.generate_policies(count)

        assert len(policies) == expected_length
        if policies:
            for policy in policies:
                assert isinstance(policy["policy_id"], str)
                assert policy["type"] in ["auto", "health", "home"]
                assert 5000 <= policy["coverage_amount"] < 50000
                assert 100 <= policy["premium"] < 1000
                assert isinstance(policy["start_date"], (str, date, datetime))
                assert isinstance(policy["end_date"], (str, date, datetime))
                assert isinstance(policy["user_id"], str)
                assert isinstance(policy["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (5, 5),
            (0, 0),
            (1, 1),
            (50, 50),
        ],
        ids=[
            "generate_five_claims",
            "generate_zero_claims",
            "generate_one_claim",
            "generate_many_claims",
        ],
    )
    def test_generate_claims(self, count: int, expected_length: int):

        claims = InsuranceEvents.generate_claims(count)

        assert len(claims) == expected_length
        if claims:
            for claim in claims:
                assert isinstance(claim["claim_id"], str)
                assert isinstance(claim["policy_id"], str)
                assert 1000 <= claim["amount_claimed"] < 20000
                assert claim["status"] in ["approved", "pending", "denied"]
                assert isinstance(claim["filed_date"], (str, date, datetime))
                assert isinstance(claim["created_at"], (str, date, datetime))

    @pytest.mark.parametrize(
        "count,expected_length",
        [
            (3, 3),
            (0, 0),
            (1, 1),
            (75, 75),
        ],
        ids=[
            "generate_three_entities",
            "generate_zero_entities",
            "generate_one_entity",
            "generate_many_entities",
        ],
    )
    def test_generate_insured_entities(self, count: int, expected_length: int):

        entities = InsuranceEvents.generate_insured_entities(count)

        assert len(entities) == expected_length
        if entities:
            for entity in entities:
                assert isinstance(entity["entity_id"], str)
                assert entity["type"] in ["vehicle", "property", "life"]
                assert isinstance(entity["description"], str)
                assert 10000 <= entity["value"] < 100000
                assert isinstance(entity["created_at"], (str, date, datetime))
