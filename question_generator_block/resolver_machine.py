from Constants import Constants
import matlab_service

class resolver_machine():
    
    APIAddress = Constants(
        NONE="", 
        MATLAB="120.72.83.82:8080", 
        EXCEL="120.72.83.82:8080",
        Default="")
    APIURL = Constants(
        NONE="/none", 
        MATLAB="/check",
        EXCEL="/check",
        Default="/none")
    NAME = Constants(
        NONE="none", 
        MATLAB="matlab",
        EXCEL="excel",
        Default="none")
    def getResolverAddress(self, query):
        if query == self.APIAddress.MATLAB:
            return self.APIAddress.MATLAB
        elif query == self.APIAddress.NONE:
            return self.APIAddress.NONE
        else:
            return self.APIAddress.NONE
    def getResolverURL(self, query):
        if query == self.APIURL.MATLAB:
            return self.APIURL.MATLAB
        elif query == self.APIURL.NONE:
            return self.APIURL.NONE
        else:
            return self.APIURL.NONE
    def getDefaultAddress(self):
        return self.APIAddress.MATLAB
    def getDefaultURL(self):
        return self.APIURL.MATLAB
    def getDefaultResolver(self):
        return self.NAME.MATLAB
    def syncCall(self, resolver, ansT, ans):
        callback = False
        if resolver == self.NAME.NONE:
            print "self.NAME.NONE"
            callback =  False       
        elif resolver == self.NAME.MATLAB:
            print "self.NAME.MATLAB:"
            callback = matlab_service.evaluate_matlab_answer(self.APIAddress.MATLAB, self.APIURL.MATLAB, ansT, ans)
        else:
            print "self.NAME.EXCEL:"
            callback = False
        
        return callback
    
if (__name__ == "__main__"):
    # Usage example.
    #Nums = Constants(
    #    ONE=1, 
    #    PI=3.14159, 
    var = resolver_machine()
    check = resolver_machine.APIAddress.MATLAB
    test = var.getResolverAddress(check)
    print test
    print '----- Following line is deliberate ValueError -----'
            
        
    
    
    
    
    
    