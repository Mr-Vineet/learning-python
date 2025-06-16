def divide(dividend, divisor):
    return dividend / divisor

def file_handling(filepath): 
    try:
        file = open(filepath, "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File is not present")
    finally:
        if 'file' in locals() and not file.closed:
            file.close()

file_handling('example.txt')

def main():
    try:
        dividend = int(input("Enter divident:"))
        divisor = int(input("Enter divisor:"))
        result = divide(dividend, divisor)
    except ValueError:
        print("Please enter valid number")
    except ZeroDivisionError:
        print("can't divide by zero")
    except Exception as ex:
        print(ex)
    else:
        print(f'Division of {dividend}/{divisor} is {result}')
        print("no error is raised")
    finally:
        print("execution completed!!")

# main()