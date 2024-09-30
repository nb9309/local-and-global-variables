# local-and-global-variables

Local and Global Variables 

-----------------------
Local variables
----------------------
=>Local variables are used in Function Body
=>The Purpose of Local Variables is that "To store Temporary Results after Function Processing".
=>Local Variables can be accessed inside of Corresponding function definition only but not possible to access other 
    part of the program (Local Access )
    
------------------------
Global Variables
------------------------
=>Global Variables are those which are used for Providing Common Value for all Different Function Definitions 
    (Global Access)
=>In Memory Management point of view, Global Variable Values takes Less Memory Space.
=>Global Variables to be defined before all the function calls(Don't Consider in between Function Definitions). So that we can  access global variable values in all those Function definitions.
=>Syntax:

---------------
			def  fun1():
			     ------------
			     ------------
			def  fun2():
			     ------------
			     ------------
			------------------
			------------------
			def  fun-n():
			     ------------
			     ------------

      #Main Program
      Var1=Val1
      Var2=val2
      --------------
      Var_n=Val_n # Here Var1,Var2,.....Var-n are called Global Variables
      fun1() # Function Call-1
      fun2() # Function Call-2
      -------
      fun-n() # Function Call-n

Hence Var1,Var2,.....Var-n are the Global Variables defined before Function Calls. 
so that We can access those values inside of corresponding Function Definitions.

------------------------------------------------------------------------------------------------------------------------------------------------------------
global key word  
======================================
=>When we want MODIFY the GLOBAL VARIABLE values in side of function defintion  then global variable names must be preceded with 'global' keyword otherwise we get "UnboundLocalError: local variable names referenced before assignment"

------------
Syntax:
-----------
	var1=val1
	var2=val2
	var-n=val-n    #  var1,var2...var-n are called global variable names.
	------------------
	def   fun1():
		------------------------
		global var1,var2...var-n
		# Modify var1,var2....var-n
	    --------------------------
	def   fun2():
	  ------------------------
	  global var1,var2...var-n
	  # Modify var1,var2....var-n
	  ---------------------------------

NOTE: To MODIFY Global variable Values inside of Function Definition, we use global Keyword (Mandatory to write)
NOTE: To ACCESS Global variable Values inside of Function Definition, we Don't use global Keyword


**global  and local variables and globals()**
	============================================
=>When we come across same global Variable names and Local Variable Names in same function definition then PVM gives preference for local variables but not for global variables.
=>In this context, to extract / retrieve the values of global variables names along with local variables, we must use globals() and it returns an object of <class,'dict'> and this dict object stores all global variable Names as Keys and global variable values as values of value.

=>Syntax:-
		var1=val1
		var2=val2
		--------------
		var-n=val-n  # var1, var2...var-n are called global Variables
		def    functionname():
		       ------------------------
		       var1=val11
		       var2=val22
		       ------------------------
		       var-n=val-nn  #  var1, var2...var-n are called local Variables
		       # Extarct  the global variables values
		       dictobj=globals()
		       ------------------------
		       globalval1=dictobj['var1']  #  or  dictobj.get("var1") or globals()['var1'] or global().get('var1')
		       globalval2=dictobj['var2']  # or dictobj.get("var2") or globals()['var2']
		       -----------------------------------------------------
