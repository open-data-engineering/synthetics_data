import logging
from src.services.account import AccountService
from src.services.audit import AuditService
from src.services.compliance import ComplianceService
from src.services.credit import CreditService
from src.services.entities import EntityService
from src.services.insurance import InsuranceService
from src.services.investments import PortfolioService
from src.services.lending import LoanService
from src.services.payment import TransactionService

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class SyntheticDataGenerator:
    def __init__(self):
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

    def generate(self):
        """Executa a inserção de dados continuamente e retorna os dados gerados."""
        all_data = {}
        logging.info("▶️  Iniciando a geração dos dados sintéticos...")
        try:
            for service, function_name, table_name, count in self.operations:

                function = getattr(service, function_name, None)

                if function and callable(function):
                    result = function(count)
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
