class Conversions: 
    def temperatureFormula(self, farenheit):
        return (farenheit - 32) * (5./9.)

    def currencyFormula(self, dollars):
        return dollars * 0.75 

    def massFormula(self, pounds):
        return pounds / 2.2

    conversionPrompts = {
            't': {
                'prompt': 'Enter a temperature in Farenheit: ',
                'function': temperatureFormula
            },  
            'c': {
                'prompt': 'Enter an amount in dollars: ',
                'function': currencyFormula 
            },
            'm': {
                'prompt': 'Enter a weight in pounds: ',
                'function': massFormula    
            }
    }

    def returnConversionPrompt(self, conversionPrompt):
        return float(raw_input(conversionPrompt))


    def setConversionFromInput(self, userSelection):
        lookupResult = self.conversionPrompts[userSelection]
        userInput = self.returnConversionPrompt(lookupResult['prompt'])
        computedValue = lookupResult['function'](self, userInput)  
        print computedValue

conversionDirection = raw_input('Convert by temperature, currency or mass (t / c / m): ')
conversions = Conversions()
conversions.setConversionFromInput(conversionDirection)
