from sketchpy import library

def main():
    try:
        obj = library.rdj()
        obj.draw()
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
