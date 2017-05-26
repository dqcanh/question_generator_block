import httplib
import json
 
 
def evaluate_matlab_answer(matlab_server_url, matlab_solver_url, teacherAns, studentAns):
 
    conn = httplib.HTTPConnection(matlab_server_url)
    headers = { "Content-Type": "application/json" }
    body = json.dumps({"teacherAns": teacherAns, "studentAns" : studentAns})
    conn.request("POST", matlab_solver_url, body, headers)
    
    response = conn.getresponse()
    if response.status == 200:
       result = json.loads(response.read())
       # print 'RESULT: ' + str(result)
       return result
    else:
        return False # error
    
    
if __name__ == "__main__":
    matlab_server_url = '172.18.10.33:8080'
    matlab_solver_url = '/solve'
    
    teacherAns =  "A =[ 2, 1, 1 ; -1, 1, -1 ; 1, 2, 3] \n B = [ 2 ; 3 ; -10] \n  InvA = inv(A) \n  X=InvA * B"
#    studentAns = "A =[ 2, 1, 1 ; -1, 1, -1 ; 1, 2, 3] \n B = [ 2 ; 3 ; -10] \n  InvA = inv(A) \n  X=InvA * B"
    studentAns = "A =[ 21, 1, 1 ; -1, 1, -1 ; 1, 2, 3] \n B = [ 2 ; 3 ; -10] \n  InvA = inv(A) \n  X=InvA * B" # Wrong answer
    
    result = evaluate_matlab_answer(matlab_server_url, matlab_solver_url, teacherAns, studentAns)
    print 'result = ' + str(result)
