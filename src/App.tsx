"use client"

import { useState } from "react"
import { Delete, RotateCcw } from "lucide-react"
import { cn } from "@/lib/utils"

interface CalculatorProps {
  className?: string
}

function ScientificCalculator({ className }: CalculatorProps = {}) {
  const [display, setDisplay] = useState("0")
  const [previousValue, setPreviousValue] = useState<number | null>(null)
  const [operation, setOperation] = useState<string | null>(null)
  const [waitingForOperand, setWaitingForOperand] = useState(false)
  const [history, setHistory] = useState<string[]>([])
  const [isScientificMode, setIsScientificMode] = useState(true)
  const [memory, setMemory] = useState<number>(0)
  const [angleMode, setAngleMode] = useState<"DEG" | "RAD">("DEG")

  const MAX_DISPLAY_LENGTH = 12

  const formatForDisplay = (value: number): string => {
    if (!isFinite(value)) {
      return value > 0 ? "Infinity" : "-Infinity"
    }
    if (isNaN(value)) {
      return "Error"
    }

    const stringValue = String(value)
    
    if (stringValue.length <= MAX_DISPLAY_LENGTH) {
      return stringValue
    }

    if (stringValue.includes('.')) {
      const [integerPart, decimalPart] = stringValue.split('.')
      const availableDecimals = MAX_DISPLAY_LENGTH - integerPart.length - 1
      
      if (availableDecimals > 0) {
        return value.toFixed(Math.min(availableDecimals, decimalPart.length))
      }
    }

    const exponential = value.toExponential()
    if (exponential.length <= MAX_DISPLAY_LENGTH) {
      return exponential
    }

    let precision = 5
    while (precision >= 0) {
      const exp = value.toExponential(precision)
      if (exp.length <= MAX_DISPLAY_LENGTH) {
        return exp
      }
      precision--
    }

    return value.toExponential(0)
  }

  const toRadians = (degrees: number) => degrees * (Math.PI / 180)
  const toDegrees = (radians: number) => radians * (180 / Math.PI)

  const inputNumber = (num: string) => {
    if (waitingForOperand) {
      setDisplay(num)
      setWaitingForOperand(false)
    } else {
      const newDisplay = display === "0" ? num : display + num
      const effectiveLength = newDisplay.replace('.', '').replace('-', '').length
      if (effectiveLength <= MAX_DISPLAY_LENGTH) {
        setDisplay(newDisplay)
      }
    }
  }

  const inputOperation = (nextOperation: string) => {
    const inputValue = Number.parseFloat(display)

    if (previousValue === null) {
      setPreviousValue(inputValue)
    } else if (operation) {
      const currentValue = previousValue || 0
      const newValue = calculate(currentValue, inputValue, operation)

      setDisplay(formatForDisplay(newValue))
      setPreviousValue(newValue)

      setHistory((prev) => [...prev.slice(-4), `${currentValue} ${operation} ${inputValue} = ${newValue}`])
    }

    setWaitingForOperand(true)
    setOperation(nextOperation)
  }

  const calculate = (firstValue: number, secondValue: number, operation: string) => {
    switch (operation) {
      case "+":
        return firstValue + secondValue
      case "-":
        return firstValue - secondValue
      case "×":
        return firstValue * secondValue
      case "÷":
        return firstValue / secondValue
      case "^":
        return Math.pow(firstValue, secondValue)
      case "=":
        return secondValue
      default:
        return secondValue
    }
  }

  const performCalculation = () => {
    const inputValue = Number.parseFloat(display)

    if (previousValue !== null && operation) {
      const newValue = calculate(previousValue, inputValue, operation)
      setDisplay(formatForDisplay(newValue))
      setHistory((prev) => [...prev.slice(-4), `${previousValue} ${operation} ${inputValue} = ${newValue}`])
      setPreviousValue(null)
      setOperation(null)
      setWaitingForOperand(true)
    }
  }

  const clear = () => {
    setDisplay("0")
    setPreviousValue(null)
    setOperation(null)
    setWaitingForOperand(false)
  }

  const clearHistory = () => {
    setHistory([])
  }

  const backspace = () => {
    if (display.length > 1) {
      setDisplay(display.slice(0, -1))
    } else {
      setDisplay("0")
    }
  }

  const factorial = (n: number): number => {
    if (n < 0 || !Number.isInteger(n)) return NaN
    if (n === 0 || n === 1) return 1
    let result = 1
    for (let i = 2; i <= n; i++) {
      result *= i
    }
    return result
  }

  const handleScientificFunction = (func: string) => {
    const currentValue = Number.parseFloat(display)
    let result: number

    switch (func) {
      case "sin":
        result = angleMode === "DEG" ? Math.sin(toRadians(currentValue)) : Math.sin(currentValue)
        break
      case "cos":
        result = angleMode === "DEG" ? Math.cos(toRadians(currentValue)) : Math.cos(currentValue)
        break
      case "tan":
        result = angleMode === "DEG" ? Math.tan(toRadians(currentValue)) : Math.tan(currentValue)
        break
      case "ln":
        result = Math.log(currentValue)
        break
      case "log":
        result = Math.log10(currentValue)
        break
      case "√":
        result = Math.sqrt(currentValue)
        break
      case "x²":
        result = currentValue * currentValue
        break
      case "x³":
        result = Math.pow(currentValue, 3)
        break
      case "1/x":
        result = 1 / currentValue
        break
      case "!":
        result = factorial(currentValue)
        break
      case "e":
        result = Math.E
        break
      case "π":
        result = Math.PI
        break
      case "∛":
        result = Math.cbrt(currentValue)
        break
      case "e^x":
        result = Math.exp(currentValue)
        break
      case "10^x":
        result = Math.pow(10, currentValue)
        break
      default:
        result = currentValue
    }

    setDisplay(formatForDisplay(result))
    setHistory((prev) => [...prev.slice(-4), `${func}(${currentValue}) = ${result}`])
    setWaitingForOperand(true)
  }

  const handleButtonClick = (btn: string) => {
    if (btn === "C") {
      clear()
    } else if (btn === "=") {
      performCalculation()
    } else if (["÷", "×", "-", "+", "^"].includes(btn)) {
      inputOperation(btn)
    } else if (btn === "±") {
      const newValue = Number.parseFloat(display) * -1
      setDisplay(formatForDisplay(newValue))
    } else if (btn === "%") {
      const newValue = Number.parseFloat(display) / 100
      setDisplay(formatForDisplay(newValue))
    } else if (btn === ".") {
      if (!display.includes(".")) {
        inputNumber(btn)
      }
    } else if (["sin", "cos", "tan", "ln", "log", "√", "x²", "x³", "1/x", "!", "e", "π", "∛", "e^x", "10^x"].includes(btn)) {
      handleScientificFunction(btn)
    } else if (btn === "MC") {
      setMemory(0)
    } else if (btn === "MR") {
      setDisplay(formatForDisplay(memory))
      setWaitingForOperand(true)
    } else if (btn === "M+") {
      setMemory(memory + Number.parseFloat(display))
    } else if (btn === "M-") {
      setMemory(memory - Number.parseFloat(display))
    } else if (btn === "DEG/RAD") {
      setAngleMode(angleMode === "DEG" ? "RAD" : "DEG")
    } else {
      inputNumber(btn)
    }
  }

  const getButtonClass = (btn: string) => {
    if (["÷", "×", "-", "+", "=", "^"].includes(btn)) {
      return "bg-orange-500 hover:bg-orange-600 text-white"
    }
    if (["C", "±", "%", "MC", "MR", "M+", "M-", "DEG/RAD"].includes(btn)) {
      return "bg-gray-500 hover:bg-gray-600 text-white"
    }
    if (["sin", "cos", "tan", "ln", "log", "√", "x²", "x³", "1/x", "!", "e", "π", "∛", "e^x", "10^x"].includes(btn)) {
      return "bg-blue-600 hover:bg-blue-700 text-white"
    }
    return "bg-gray-700 hover:bg-gray-600 text-white"
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 flex items-center justify-center p-4">
      <div className={cn("bg-gray-900 rounded-lg p-4 w-full max-w-md flex flex-col shadow-2xl", className)}>
        <div className="flex items-center justify-between mb-3">
          <h3 className="text-white font-semibold text-lg">Calculadora Científica</h3>
          <div className="flex space-x-2">
            <button
              onClick={() => setIsScientificMode(!isScientificMode)}
              className="text-xs bg-blue-600 hover:bg-blue-700 text-white px-2 py-1 rounded transition-colors"
            >
              {isScientificMode ? "Básica" : "Científica"}
            </button>
            <button onClick={backspace} className="text-gray-400 hover:text-white transition-colors">
              <Delete size={16} />
            </button>
            <button onClick={clearHistory} className="text-gray-400 hover:text-white transition-colors">
              <RotateCcw size={16} />
            </button>
          </div>
        </div>

        {/* History */}
        <div className="bg-gray-800 rounded p-2 mb-3 h-16 overflow-y-auto">
          {history.length > 0 ? (
            <div className="space-y-1">
              {history.slice(-3).map((entry, index) => (
                <div key={index} className="text-xs text-gray-400">
                  {entry}
                </div>
              ))}
            </div>
          ) : (
            <div className="text-xs text-gray-500">Histórico aparecerá aqui</div>
          )}
        </div>

        {/* Display */}
        <div className="bg-black rounded p-4 mb-3 text-right">
          <div className="flex justify-between items-center mb-1">
            <div className="text-xs text-gray-400">
              {memory !== 0 && <span className="mr-2">M</span>}
              <span>{angleMode}</span>
            </div>
            {operation && (
              <div className="text-orange-400 text-sm">
                {previousValue} {operation}
              </div>
            )}
          </div>
          <div className="text-white text-3xl font-mono overflow-hidden">{display}</div>
        </div>

        {/* Buttons */}
        <div className="grid grid-cols-5 gap-2">
          {isScientificMode && (
            <>
              {/* Scientific Row 1 */}
              <button onClick={() => handleButtonClick("DEG/RAD")} className={`${getButtonClass("DEG/RAD")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>{angleMode}</button>
              <button onClick={() => handleButtonClick("sin")} className={`${getButtonClass("sin")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>sin</button>
              <button onClick={() => handleButtonClick("cos")} className={`${getButtonClass("cos")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>cos</button>
              <button onClick={() => handleButtonClick("tan")} className={`${getButtonClass("tan")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>tan</button>
              <button onClick={() => handleButtonClick("^")} className={`${getButtonClass("^")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>x^y</button>
              
              {/* Scientific Row 2 */}
              <button onClick={() => handleButtonClick("ln")} className={`${getButtonClass("ln")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>ln</button>
              <button onClick={() => handleButtonClick("log")} className={`${getButtonClass("log")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>log</button>
              <button onClick={() => handleButtonClick("√")} className={`${getButtonClass("√")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>√</button>
              <button onClick={() => handleButtonClick("∛")} className={`${getButtonClass("∛")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>∛</button>
              <button onClick={() => handleButtonClick("!")} className={`${getButtonClass("!")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>n!</button>
              
              {/* Scientific Row 3 */}
              <button onClick={() => handleButtonClick("x²")} className={`${getButtonClass("x²")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>x²</button>
              <button onClick={() => handleButtonClick("x³")} className={`${getButtonClass("x³")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>x³</button>
              <button onClick={() => handleButtonClick("1/x")} className={`${getButtonClass("1/x")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>1/x</button>
              <button onClick={() => handleButtonClick("e^x")} className={`${getButtonClass("e^x")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>e^x</button>
              <button onClick={() => handleButtonClick("10^x")} className={`${getButtonClass("10^x")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>10^x</button>
              
              {/* Scientific Row 4 */}
              <button onClick={() => handleButtonClick("MC")} className={`${getButtonClass("MC")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>MC</button>
              <button onClick={() => handleButtonClick("MR")} className={`${getButtonClass("MR")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>MR</button>
              <button onClick={() => handleButtonClick("M+")} className={`${getButtonClass("M+")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>M+</button>
              <button onClick={() => handleButtonClick("M-")} className={`${getButtonClass("M-")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>M-</button>
              <button onClick={() => handleButtonClick("π")} className={`${getButtonClass("π")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>π</button>
            </>
          )}
          
          {/* Basic Calculator Row 1 */}
          <button onClick={() => handleButtonClick("C")} className={`${getButtonClass("C")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>C</button>
          <button onClick={() => handleButtonClick("±")} className={`${getButtonClass("±")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>±</button>
          <button onClick={() => handleButtonClick("%")} className={`${getButtonClass("%")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>%</button>
          <button onClick={() => handleButtonClick("÷")} className={`${getButtonClass("÷")} h-12 rounded text-lg font-semibold transition-colors active:scale-95 ${!isScientificMode ? 'col-span-2' : ''}`}>÷</button>
          {isScientificMode && <button onClick={() => handleButtonClick("e")} className={`${getButtonClass("e")} h-12 rounded text-xs font-semibold transition-colors active:scale-95`}>e</button>}
          
          {/* Row 2 */}
          <button onClick={() => handleButtonClick("7")} className={`${getButtonClass("7")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>7</button>
          <button onClick={() => handleButtonClick("8")} className={`${getButtonClass("8")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>8</button>
          <button onClick={() => handleButtonClick("9")} className={`${getButtonClass("9")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>9</button>
          <button onClick={() => handleButtonClick("×")} className={`${getButtonClass("×")} h-12 rounded text-lg font-semibold transition-colors active:scale-95 ${!isScientificMode ? 'col-span-2' : ''}`}>×</button>
          {isScientificMode && <div className="h-12"></div>}
          
          {/* Row 3 */}
          <button onClick={() => handleButtonClick("4")} className={`${getButtonClass("4")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>4</button>
          <button onClick={() => handleButtonClick("5")} className={`${getButtonClass("5")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>5</button>
          <button onClick={() => handleButtonClick("6")} className={`${getButtonClass("6")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>6</button>
          <button onClick={() => handleButtonClick("-")} className={`${getButtonClass("-")} h-12 rounded text-lg font-semibold transition-colors active:scale-95 ${!isScientificMode ? 'col-span-2' : ''}`}>-</button>
          {isScientificMode && <div className="h-12"></div>}
          
          {/* Row 4 */}
          <button onClick={() => handleButtonClick("1")} className={`${getButtonClass("1")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>1</button>
          <button onClick={() => handleButtonClick("2")} className={`${getButtonClass("2")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>2</button>
          <button onClick={() => handleButtonClick("3")} className={`${getButtonClass("3")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>3</button>
          <button onClick={() => handleButtonClick("+")} className={`${getButtonClass("+")} h-12 rounded text-lg font-semibold transition-colors active:scale-95 ${!isScientificMode ? 'col-span-2' : ''}`}>+</button>
          {isScientificMode && <div className="h-12"></div>}
          
          {/* Row 5 */}
          <button onClick={() => handleButtonClick("0")} className={`${getButtonClass("0")} h-12 rounded text-lg font-semibold transition-colors active:scale-95 col-span-2`}>0</button>
          <button onClick={() => handleButtonClick(".")} className={`${getButtonClass(".")} h-12 rounded text-lg font-semibold transition-colors active:scale-95`}>.</button>
          <button onClick={() => handleButtonClick("=")} className={`${getButtonClass("=")} h-12 rounded text-lg font-semibold transition-colors active:scale-95 ${isScientificMode ? 'col-span-2' : 'col-span-2'}`}>=</button>
        </div>
      </div>
    </div>
  )
}

export default function App() {
  return <ScientificCalculator />
}

