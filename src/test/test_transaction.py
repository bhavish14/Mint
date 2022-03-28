from datetime import datetime
from typing import List
import unittest

from transaction.transaction import Transaction


class TestTransactionClass(unittest.TestCase):
    """
        Mint Transaction testing class wrapper
    """

    @classmethod
    def setUpClass(cls):
        print('Starting tests for transactions class.')

    def test_transaction_class_init(self) -> None:
        """
            Tests the initialization of a Mint Transaction object
        """
        transaction_object: Transaction = Transaction()
        self.assertEqual(
            transaction_object.date,
            None,
            'Should be None'
        )
        self.assertEqual(
            transaction_object.original_description,
            None,
            'Should be None'
        )
        self.assertEqual(
            transaction_object.description,
            None,
            'Should be None'
        )
        self.assertEqual(
            transaction_object.amount,
            None,
            'Should be None'
        )
        self.assertEqual(
            transaction_object.transaction_type,
            None,
            'Should be None'
        )
        self.assertEqual(
            transaction_object.category,
            None,
            'Should be None'
        )
        self.assertEqual(
            transaction_object.account_name,
            None,
            'Should be None'
        )
        self.assertEqual(transaction_object.label, None, 'Should be None')
        self.assertEqual(transaction_object.notes, None, 'Should be None')

    def test_load_transaction_1(self) -> None:
        """
            Tests the loading of transaction object with an empty list
        """
        transaction_object: Transaction = Transaction()

        self.assertRaises(
            ValueError,
            transaction_object.load_transaction,
            'Test case :: test_load_transaction_1 failed.'
        )

    def test_load_transaction_2(self) -> None:
        """
            Tests the loading of transaction object with invalid date
        """
        transaction_object: Transaction = Transaction()
        test_transaction: List[str] = [
            123,
            'Test Transaction',
            'Test Transaction',
            '25.00',
            'debit',
            'test-category',
            'test-account',
            'test-label',
            'test-notes'
        ]

        self.assertRaises(
            TypeError,
            transaction_object.load_transaction,
            test_transaction
        )

    def test_load_transaction_3(self) -> None:
        """
            Tests the loading of transaction object with all valid values
        """
        transaction_object: Transaction = Transaction()
        test_transaction: List[str] = [
            '3/11/2022',
            'Test Transaction',
            'Test Transaction',
            '25.00',
            'debit',
            'test-category',
            'test-account',
            'test-label',
            'test-notes'
        ]

        transaction_object.load_transaction(test_transaction)

        self.assertEqual(
            transaction_object.date,
            datetime(2022, 3, 11, 0, 0),
            'Should be None'
        )
        self.assertEqual(
            transaction_object.original_description,
            'Test Transaction',
            'Should be None'
        )
        self.assertEqual(
            transaction_object.description,
            'Test Transaction',
            'Should be None'
        )
        self.assertEqual(
            transaction_object.amount,
            '25.00',
            'Should be None'
        )
        self.assertEqual(
            transaction_object.transaction_type,
            'debit',
            'Should be None'
        )
        self.assertEqual(
            transaction_object.category,
            'test-category',
            'Should be None'
        )
        self.assertEqual(
            transaction_object.account_name,
            'test-account',
            'Should be None'
        )
        self.assertEqual(
            transaction_object.label,
            'test-label',
            'Should be None'
        )
        self.assertEqual(
            transaction_object.notes,
            'test-notes',
            'Should be None'
        )


if __name__ == '__main__':
    unittest.main()
