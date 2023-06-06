#Let us see the access modifiers in Python to understand the concept of Encapsulation and data hiding −

#1. public: The public member is accessible from inside or outside the class.
#2. private: The private member is accessible only inside class. Define a private member by prefixing the member name with two underscores, for example − __age
#3. protected: Protected means that the attribute/method can only be used in the class where it is defined or its subclasses.


class Thing:
    def __init__(self, public: str, *, protected: str = "protected", private: str = "private"):
        self.public = public
        self._protected = protected
        self.__private = private

    def info(self) -> None:
        print(
            (
                f"This class has public attribute: {self.public}, "
                f"protected attribute: {self._protected}, "
                f"and private attribute: {self.__private}"
            )
        )
        
class SomeThing(Thing):
    def _more_info(self) -> None:
        print(f"This class has public attribute: {self.public}, protected attribute: {self._protected}")

    def use_private(self) -> None:
        self._more_info()
        #print(f"Private attribute is {self.__private}")
        
thing = Thing("public")
thing.info() #accessing the variables internally
print(thing.public) #runs
print(thing._protected) #runs
# print(thing.__private) #dont run

some_thing = SomeThing("public")
some_thing.use_private() #accessing the protected variable with sub class
# some_thing.use_private() # will not run as private is not accessible

