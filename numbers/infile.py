
class DataFiles:

    def __init__(self, file_name: str, target: int=None):
        self.path = file_name
        self.target = target

    # What i need to happen is: the file gets passed into the read input.
    # The file is read and the numbers are all queried in an array
    # The functions sorts the array and determines the largest overall number
    def largest_number_in_file(self):
        numbers = []

        with open(self.path, 'r') as data_file:
            nums = data_file.readlines()
            for num in nums:
                numbers.append(num.strip())

        # Get the largest number in the numbers array
        # Init the max content variable
        max_content = numbers[0]

        # Traverse array elements from second
        # and compare every element with
        # the current max
        for i in range(1, len(numbers)):
            if numbers[i] > max_content:
                max_content = numbers[i]

        return max_content