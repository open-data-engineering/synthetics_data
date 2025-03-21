import logging
from services.account import AccountService
from services.audit import AuditService
from services.compliance import ComplianceService
from services.credit import CreditService
from services.entities import EntityService
from services.insurance import InsuranceService
from services.investments import PortfolioService
from services.lending import LoanService
from services.payment import TransactionService

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class SyntheticDataGenerator:
    """Generates synthetic data for various services.

    This class orchestrates the generation of synthetic data for different services
    by calling their respective insertion functions.
    """

    def __init__(self):
        """Initializes the SyntheticDataGenerator with a list of operations."""
        self.operations = [
            (AccountService, "insert_users", "users", 20000),
            (AccountService, "insert_accounts", "accounts", 20000),
            (AccountService, "insert_subaccounts", "subaccounts", 20000),
            (AuditService, "insert_audits", "audits", 20000),
            (ComplianceService, "insert_regulations", "regulations", 20000),
            (ComplianceService, "insert_user_verification", "user_verification", 20000),
            (CreditService, "insert_credit_scores", "credit_scores", 20000),
            (CreditService, "insert_risk_assessments", "risk_assessments", 20000),
            (EntityService, "insert_entities", "entities", 20000),
            (InsuranceService, "insert_policies", "policies", 20000),
            (InsuranceService, "insert_claims", "claims", 20000),
            (InsuranceService, "insert_insured_entities", "insured_entities", 20000),
            (PortfolioService, "insert_portfolios", "portfolios", 20000),
            (LoanService, "insert_loans", "loans", 20000),
            (LoanService, "insert_payments", "loan_payments", 20000),
            (TransactionService, "insert_transactions", "transactions", 20000),
            (TransactionService, "insert_payment_methods", "payment_methods", 20000),
            (TransactionService, "insert_merchants", "merchants", 20000),
        ]

    def generate(self, override_counts: dict = None):
        """Generates synthetic data for all services.

        This method iterates through the defined operations, retrieves the corresponding
        service function, and executes it to generate synthetic data. The generated data
        is stored in a dictionary where keys are table names and values are the data.
        """
        all_data = {}
        logging.info("▶️  Iniciando a geração dos dados sintéticos...")
        try:
            for service, function_name, table_name, count in self.operations:
                effective_count = (
                    override_counts.get(table_name, count) if override_counts else count
                )

                function = getattr(service, function_name, None)

                if function and callable(function):
                    result = function(effective_count)
                    all_data[table_name] = result
                else:
                    logging.error(
                        f"❌ {function_name} não encontrado no {service.__name__}"
                    )

            logging.info("✅ Dados sintéticos gerados com sucesso!")
            return all_data

        except Exception as e:
            logging.error(f"❌ Erro durante o ciclo de inserção: {e}")
            return {}
