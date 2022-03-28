from typing import IO, List, Set, Dict
import csv

from transaction.transaction import Transaction


class Mint:
    '''
        Mint class
    '''

    def __init__(
        self,
        transactions_file_path: str
    ) -> None:
        try:
            self.transactions_file_path: str = transactions_file_path
            self.transactions_file: IO = None
            self.transactions: List[Transaction] = []

            # load transactions file
            self.load_transactions_file()

            # skip header
            next(self.transactions_file)

            for row in self.transactions_file:
                transaction_obj: Transaction = Transaction()
                transaction_obj.load_transaction(row)
                self.transactions.append(transaction_obj)

        except Exception as err:
            print(err)
            raise

    def load_transactions_file(self) -> bool:
        '''
            Loads contents of transactions file
        '''
        try:
            if not self.transactions_file_path:
                raise FileNotFoundError(
                    f'Transactions file not found at {self.transactions_file_path}'
                )

            self.transactions_file = csv.reader(
                open(
                    file=self.transactions_file_path,
                    mode='r',
                    encoding='utf-8'
                )
            )

        except:
            raise

    def summarize_trasactions_by_category(self) -> Dict:
        """
            Summarizes transactions by category
        """
        try:
            category_totals: Dict = {}

            for transaction in self.transactions:
                if transaction.category not in category_totals:
                    category_totals[transaction.category] = 0

                category_totals[transaction.category] \
                    += float(transaction.amount)

            for category, value in category_totals.items():
                category_totals[category] = round(value, 2)

            return category_totals
        except Exception as err:
            print(err)
            raise
