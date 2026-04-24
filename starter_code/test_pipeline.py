import unittest
import os
import pandas as pd
from process_csv import process_sales_csv
from process_html import parse_html_catalog

class TestDataPipeline(unittest.TestCase):
    def setUp(self):
        self.csv_path = 'test_sales.csv'
        pd.DataFrame({
            'id': [1, 2, 2, 3, 4],
            'price': ["$1200", "250,000", "250,000", "five dollars", "15.99 USD"],
            'date_of_sale': ["12/31/2022", "2023-01-05", "2023-01-05", "Bad Date", "15 Feb 2023"]
        }).to_csv(self.csv_path, index=False)
        
        self.html_path = 'test_catalog.html'
        with open(self.html_path, 'w', encoding='utf-8') as f:
            f.write('''<table id="main-catalog">
                <tr><th>id</th><th>name</th><th>price</th></tr>
                <tr><td>1</td><td>Product 1</td><td>$100.50</td></tr>
                <tr><td>2</td><td>Product 2</td><td>N/A</td></tr>
                <tr><td>3</td><td>Product 3</td><td>Liên hệ</td></tr>
                <tr><td>4</td><td>Product 4</td><td>999</td></tr>
            </table>''')

    def tearDown(self):
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
        if os.path.exists(self.html_path):
            os.remove(self.html_path)

    def test_process_csv(self):
        docs = process_sales_csv(self.csv_path)
        
        self.assertEqual(len(docs), 4)
        self.assertEqual(docs[0]['source_metadata']['price'], 1200.0)
        self.assertEqual(docs[1]['source_metadata']['price'], 250000.0)
        self.assertEqual(docs[2]['source_metadata']['price'], 0.0)
        self.assertEqual(docs[3]['source_metadata']['price'], 15.99)
        self.assertEqual(docs[0]['source_metadata']['date_of_sale'], '2022-12-31')
        self.assertEqual(docs[2]['source_metadata']['date_of_sale'], '')
        
    def test_process_html(self):
        docs = parse_html_catalog(self.html_path)
        
        self.assertEqual(len(docs), 4)
        self.assertEqual(docs[0]['source_metadata']['price'], 100.50)
        self.assertEqual(docs[1]['source_metadata']['price'], 0.0)
        self.assertEqual(docs[2]['source_metadata']['price'], 0.0)
        self.assertEqual(docs[3]['source_metadata']['price'], 999.0)

if __name__ == '__main__':
    unittest.main()
