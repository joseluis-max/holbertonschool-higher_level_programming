# Almost Circle
## *Args and **kwargs.

> **_NOTE:_** First of all let me tell you that it is not necessary to write `*args` or `**kwargs`. Only the * is necessary.  You could have also written *var and **vars. Writing `*args` and `**kwargs` is just a convention.

## Usage of  *args and **kwargs.

`*args` and `**kwargs` are mostly used in functions definitions, allow you to pass a variable number of arguments to a function.

__*Args__
`*args` and `**kwargs` are mostly used in functions definitions, allow you to pass a variable number of arguments to a function.

```python
def test_var_args(f_arg, *argv):
  print "First nornal arg:", f_arg
	  for arg in argv:
		  print "Another arg through *argv: ", arg

test_var_args('yasoob','python','eggs','test')
```
This produces the following result:
```
first normal arg: yasoob
another arg through *argv : python
another arg through *argv : eggs
another arg through *argv : test
```

__**kwargs__
`**kwargs` allows you to pass **keyworded**  variable length of arguments to 
a function. You should use it  if you want to handle **named arguments** in 
a function.

```python
def greet_me(**kwargs):
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      print "%s == %s" %(key,value)
 
>>> greet_me(name="yasoob", last_name="Valdiviezo")
name == yasoob
last_name == Valdiviezo
```

## *args and **kwargs to call a function with list or dictionary

So here we will see how to call a function using `*args` and `**kwargs`. Just consider that you have this little function:

```python
def test_args_kwargs(arg1, arg2, arg3):
  print "arg1:", arg1
  print "arg2:", arg2
  print "arg3:", arg3
```
Now you can use `*args` or `**kwargs` to pass arguments to this little function. Here’s how to do it:

 ```python
 # first with *args
>>> args = ("two", 3,5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# now with **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two","arg1":5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```
## Order of using *args, **kwargs and formal args
So if you want to use all three of these in functions then the order is:

```
some_func(fargs,*args,**kwargs)
```
