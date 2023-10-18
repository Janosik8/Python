def funkcja2(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, *args, *kwargs)

funkcja2('jeden', 'dwa', 1, 123, trzy='trzy', siedem='osiem')