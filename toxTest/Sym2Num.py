def sym2num():
    #at the moment we fake
    import sympy
    import pkg_resources
    v=pkg_resources.get_distribution('sympy').version
    if v=='1.0': 
        return(42)
    raise(Exception('The sympy Version is not compatible'))

