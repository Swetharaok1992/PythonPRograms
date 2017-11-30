import math

class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

	# returns the number of items within the entire collection
    def item_count(self):
        self.count = len(self.collection)
        return self.count

	# returns the number of pages
    def page_count(self):
        count = 1
        index = 0
        second_index = 0
        # creates the items in a list based on the input given
        page_list = [[0] * self.items_per_page for i in range(math.ceil(len(self.collection)/self.items_per_page))]
        for item in self.collection:
            # Adds data to the the 2D list
            if(count > self.items_per_page):
                count = 1
                second_index = 0
                index = index + 1
            page_list[index][second_index] = item
            second_index += 1
            count = count + 1


        return page_list

	# returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        temp_list = self.page_count()
        list_end_count = 0
        remove_list = False
        length_list = -1
        value_pages = math.ceil(len(self.collection)/self.items_per_page)
        # returns the number of items in the current page
        if page_index < value_pages:
            for temp_count,temp_item in enumerate(temp_list[page_index]):
                if(temp_item == 0):
                    remove_list = True
                    list_end_count = temp_count
                    break
            if remove_list == True:
                del temp_list[page_index][list_end_count:]
                remove_list = False
            length_list = len(temp_list[page_index])
        return length_list


	# determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        p_index = -1
        index_count = 0
        indx1 = 0
        indx2 = 0
        torf  = False
        for icount, itr in enumerate(self.page_count()):
            for cnt, iter in enumerate(itr):
                if iter == 0:
                    torf = True
                    indx1 = icount
                    indx2 = cnt
                    break
        # Checks if the item in the list and the item entered by the user is same then return the page number where the item is in
        if torf == True:
            p_list = self.page_count()
            del p_list[indx1][indx2:]
            for ic, it in enumerate(p_list):
                for ct,ptr in enumerate(it):
                    if index_count == item_index:
                        p_index = ic
                    index_count += 1
        return p_index
# The file consisting of data is read and stored as a list. An object to the class PaginationHelper  is created and list and pages number
# is passed to the constructor and various methods in the class is called and the returned value is displayed.
try:
    helper_list = list()
    with open("E:\\University Of Bridgeport\\Fall 2017\\Python\\Assignment-Ques\\Characters_read.txt", "r", encoding="utf-8-sig")as page_helper:
        helper_list = (page_helper.read()).split(",")
        helper = PaginationHelper(helper_list, 5)
        print("Page count: " + str(len(helper.page_count())))
        print("Item count: " + str(helper.item_count()))
        print("Page item count: " + str(helper.page_item_count(0)))
        print("Page index: " + str(helper.page_index(23)))

except IOError:
    print("Could not open file for reading.")

except:
    print("An error occurred")



