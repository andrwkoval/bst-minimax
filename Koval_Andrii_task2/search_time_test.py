from Koval_Andrii_task2.linkedbst import LinkedBST
import time
import random

SAMPLE_SIZE = 10000


def read_file():
    """
    param path_file:
    return:
    """
    with open("words.txt", "r", encoding="utf-8", errors="ignore") as f:
        words = [i.strip() for i in f]
    return words


def sample():
    """
    :return:
    """
    words = read_file()
    return [random.choice(words) for i in range(SAMPLE_SIZE)]


def create_tree(words):
    """
    param words:
    return:
    """
    bst = LinkedBST()
    for i in set(words):
        bst.add(i)
    return bst


def find_words_list(words):
    """
    :return:
    """
    start = time.time()
    [words.index(i) for i in sample()]
    return time.time() - start


def find_words_bst_unbalanced(tree):
    """
    :param tree:
    :return:
    """
    start = time.time()
    for i in sample():
        tree.find(i)
    return time.time() - start


def find_words_bst_balanced(tree):
    """
    :param tree:
    :return:
    """
    tree.rebalance()
    start = time.time()
    for i in sample():
        tree.find(i)
    return time.time() - start


if __name__ == "__main__":
    words = read_file()
    tree = create_tree(words)
    print("Start testing...\n")
    list_time = find_words_list(words)
    unbalanced_bst = find_words_bst_unbalanced(tree)
    balanced_bst = find_words_bst_balanced(tree)
    print(f"Time for searching {SAMPLE_SIZE} words in list is : |{list_time}|")
    print(f"Time for searching {SAMPLE_SIZE} words in unbalanced Binary Tree "
          f"is : |{unbalanced_bst}|")
    print(f"Time for searching {SAMPLE_SIZE} words in balanced Binary Tree "
          f"is : |{balanced_bst}|")
    print("\n...finish testing.")

