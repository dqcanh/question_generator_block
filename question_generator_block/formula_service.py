import cexprtk


def is_int(value):
  try:
    int(value)
    return True
  except:
    return False


def evaluate_submission(variable_values, expression_values):
    """
    Evaluates whether a submission is correct with respect to variable values and expression values
    
    Parameters:
        + variable_values: a dict in which each element is { variable name: [ variable instance, variable value ]}
        + expression_values: a dict in which each element is { expression name: [ expression instance, expression value of student ] }
    
    Returns:
        + a dict in which each element is (expression_name: 0 / 1) indicating whether the corresponding expression value is correct (1) or not (0) with respect to the expression formula
    """
    
    expressions = {}
    for expr_name, expr_data in expression_values.iteritems():
        expressions[expr_name] = expr_data[0]
    
    cexprtk_expression_values = evaluate_expressions(variable_values, expressions)
    
    result = {} # result (expression name : 0 / 1)
    for expr_name, expr_data in expression_values.iteritems():
        expression = expr_data[0]
        student_expression_value = expr_data[1]
#        expr_formula = expression['formula'] # BUG why this is unicode????
        expr_type = expression['type']
        expr_val_decimal_places = int(expression['decimal_places'])
        coerced_student_expression_value = 0
        
        if expr_type == 'int': # integer
            if is_int(student_expression_value):
                coerced_student_expression_value = int(student_expression_value)
            else:
                coerced_student_expression_value = int(float(student_expression_value))
        else: # float TODO use Decimal
            coerced_student_expression_value = float(student_expression_value)
    
        # compare the student's result
        if (expr_type == 'int'):
            expr_val_decimal_places = 0
        if (areAlmostEqual(coerced_student_expression_value, cexprtk_expression_values[expr_name], expr_val_decimal_places)):
            result[expr_name] = 1
        else:
            result[expr_name] = 0
    
    return result


def evaluate_expressions(variable_values, expressions):
    """
    Evaluates the expressions with respect to the variable values.
    
    Parameters:
        + variables_values: a dict in which each element is { variables name : [ variable instance, variable value ] } 
        + expressions: a dict in which each element is { expression name : expression instance }
        
    Returns:
        + a dict in which each element is { expression name : expression value }
    """
    cexprtk_variables = {} # variable_name : variable_value
    result = {} # result (expression name : 0 / 1)
    
    for var_name, var_data in variable_values.iteritems():
        variable = var_data[0]
        var_value = 0
        var_type = variable['type']
        
        if var_type == 'int':  # integer
            if (is_int(var_data[1])):
                var_value = int(var_data[1])
            else:
                var_value = int(float(var_data[1]))
        else: # float
            var_value = float(var_data[1])
        
        cexprtk_variables[var_name] = var_value
    
    
    #    create SymbolTable
    symbol_table = cexprtk.Symbol_Table(cexprtk_variables, add_constants= True)

    for expr_name, expression in expressions.iteritems():
        expr_formula = expression['formula'] # BUG why this is unicode????
        expr_type = expression['type']
        decimal_places = expression['decimal_places']
        
        cexprtk_expression = cexprtk.Expression(expr_formula.encode('utf-8'), symbol_table) # remove unicode: http://stackoverflow.com/questions/4855645/how-to-turn-unicode-strings-into-regular-strings
        cexprtk_expression_value = cexprtk_expression.value()
        
        # perform the rounding appropriately
        if (expr_type == 'int'):
            result[expr_name] = round(cexprtk_expression_value, 0)
        else:
            result[expr_name] = round(cexprtk_expression_value, decimal_places) # ??? http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
        
    
    return result


def check_expressions(expressions):
    """
    Checks whether the expressions are parse-able
    """
    not_parseable_expressions = {}
    
    for expr_name, expression in expressions.iteritems():
        expr_formula = expression['formula'] # BUG why this is unicode????
        
        try:
            cexprtk.check_expression(expr_formula)
        except cexprtk.ParseException:
            not_parseable_expressions[expr_name] = expr_formula
        
    # TODO check that the expressions can be evaluated also
    return not_parseable_expressions


def areAlmostEqual(first, second, places=None, msg=None, delta=None):
    """
        Note: Inspired by unittest.TestCase's 'assertAlmostEquals' method
        
        Fail if the two objects are unequal as determined by their
       difference rounded to the given number of decimal places
       (default 7) and comparing to zero, or by comparing that the
       between the two objects is more than the given delta.
    
       Note that decimal places (from zero) are usually not the same
       as significant digits (measured from the most significant digit).
    
       If the two objects compare equal then they will automatically
       compare almost equal.
    """
    if first == second:
        # shortcut
        return True
    
    if delta is not None and places is not None:
        raise TypeError("specify delta or places not both")
    
    if delta is not None:
        if abs(first - second) <= delta:
            return True
    
    else:
        if places is None:
            places = 7
    
        if round(abs(second-first), places) == 0:
            return True
    
    return False
    
    
    