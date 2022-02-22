import inspect
from reflect import reflect
import cbpro

def main():
    print("\n ################################################ \n Python Reflections Library, Base Engine Is Running.\n ################################################ \n ")
    print(reflect._module_info(cbpro))
    # print(reflect.get_user_attributes(PublicClient))

if __name__ == "__main__":
        main ()
