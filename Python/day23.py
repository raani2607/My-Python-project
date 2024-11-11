# Assertion -> statement that check or test if a condition in your codebase is true and if its not then false

def avg(mark):

    assert len(mark) != 0, "bro add sth in your list"
    return sum(mark) / len(mark)

result = [11,22,42]
result1 = []
print(f"the result of the average is : ", avg(result1))