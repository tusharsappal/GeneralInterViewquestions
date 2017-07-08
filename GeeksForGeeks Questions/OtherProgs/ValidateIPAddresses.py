class ValidateIpAddress(object):

    def validateIpAddresses(self, ipAddress):
        # First we will separate the string by the '.'
        listOfParts = ipAddress.split(".")
        lenghtOfIpAddress = len(listOfParts)
        ipAddressValidity = False

        for element in listOfParts:
            isDigit = element.isdigit()
            if isDigit == True:
                if int(element) < 0 or int(element) > 255 or lenghtOfIpAddress != 4:
                    ipAddressValidity = False
                else:
                    ipAddressValidity = True
            else:
                ipAddressValidity = False

        if ipAddressValidity is True:
            print "The IP Address is valid"
        else:
            print "The IP Address is not valid"


if __name__ == "__main__":
    validate = ValidateIpAddress()

    validate.validateIpAddresses("128.0.0.1")
    validate.validateIpAddresses("125.16.100.1")
    validate.validateIpAddresses("125.512.100.1")
    validate.validateIpAddresses("125.512.100.abc")
    validate.validateIpAddresses("125.512.100")
