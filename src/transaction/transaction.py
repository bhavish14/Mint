from datetime import date, datetime
from typing import List


class Transaction:
    """
        Wrapper for mint transactions
    """

    def __init__(self) -> None:
        try:
            self.date: date = None
            self.description: str = None
            self.original_description: str = None
            self.amount: str = None
            self.transaction_type: str = None
            self.category: str = None
            self.account_name: str = None
            self.label: str = None
            self.notes: str = None
        except:
            raise

    def load_transaction(self, transaction: List[str]) -> None:
        """
            Loads mint transaction row into MintTransaction object

            Args:
                transaction (List[str]): Values of transaction

            Returns:
                None

            Raises:
                ValueError: If the transaction does not contain all the required values
        """
        try:

            if len(transaction) != 9:
                raise ValueError(
                    'Transaction row does not have all the required fields'
                )

            [
                self.date,
                self.description,
                self.original_description,
                self.amount,
                self.transaction_type,
                self.category,
                self.account_name,
                self.label,
                self.notes
            ] = transaction

            # format date
            self.date = datetime.strptime(self.date, '%m/%d/%Y')
        except:
            raise

    def __str__(self) -> str:
        """
            Represents the MintTransaction object as a string using the following format
            <MintTransaction> <month day, year> :: <transaction type> :: <category> :: <account> :: <amount>

            Args:
                None

            Returns:
                MintTransaction represented as a string
        """
        return f'{"<MintTransaction>":20} {self.date.strftime("%b %d, %Y"):10} \
            :: {self.transaction_type:10} :: {self.category:20} :: {self.account_name:20} :: $ {self.amount:20}'

    def generate_sankey_string(self) -> str:
        """
            Loads mint transaction row into MintTransaction object

            Args:
                transaction (List[str]): Values of transaction

            Returns:
                None

            Raises:
                ValueError: If the transaction does not contain all the required values
        """
        try:
            return f'{self.category} [{self.amount}] {self.category}'
        except:
            raise
