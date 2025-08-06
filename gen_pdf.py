import pdfplumber
import numpy as np
import matplotlib.pyplot as plt

def generate_pdf_statistics(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        page_word_counts = []
        for page in pdf.pages:
            text = page.extract_text()
            word_count = len(text.split())
            page_word_counts.append(word_count)

        # Calculate statistics
        total_pages = len(page_word_counts)
        avg_words_per_page = np.mean(page_word_counts)
        max_words_page = np.max(page_word_counts)

        # Print stats
        print(f"Total Pages: {total_pages}")
        print(f"Average Words per Page: {avg_words_per_page}")
        print(f"Maximum Words on a Page: {max_words_page}")

        # Plot histogram of words per page
        plt.hist(page_word_counts, bins=10, color='blue', edgecolor='black')
        plt.title('Distribution of Words per Page')
        plt.xlabel('Number of Words')
        plt.ylabel('Frequency')
        plt.show()

# Example usage
generate_pdf_statistics('Offcampus for Girls(All Resources SDE).pdf')




