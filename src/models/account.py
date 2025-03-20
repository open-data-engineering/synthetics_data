from datetime import datetime

class User:
    def __init__(self, user_id: str, name: str, email: str, phone: str, created_at: datetime):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.created_at = created_at

    def to_dict(self):
        """Converte a instância para dicionário serializável."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }

class Account:
    def __init__(self, account_id: str, account_type: str, balance: int, currency: str, status: str, user_id: str, created_at: datetime):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.currency = currency
        self.status = status
        self.user_id = user_id
        self.created_at = created_at

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "account_type": self.account_type,
            "balance": self.balance,
            "currency": self.currency,
            "status": self.status,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }

class Subaccount:
    def __init__(self, subaccount_id: str, parent_account_id: str, purpose: str, balance: int, created_at: datetime):
        self.subaccount_id = subaccount_id
        self.parent_account_id = parent_account_id
        self.purpose = purpose
        self.balance = balance
        self.created_at = created_at

    def to_dict(self):
        return {
            "subaccount_id": self.subaccount_id,
            "parent_account_id": self.parent_account_id,
            "purpose": self.purpose,
            "balance": self.balance,
            "created_at": self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }