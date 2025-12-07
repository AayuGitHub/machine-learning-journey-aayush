import React, { useState, useEffect } from 'react';

type Operation = '+' | '-' | '*' | '/' | '^' | null;

const Calculator: React.FC = () => {
    const [input, setInput] = useState<string>('0');
    const [previousVal, setPreviousVal] = useState<number | null>(null);
    const [operation, setOperation] = useState<Operation>(null);
    const [waitingForNewInput, setWaitingForNewInput] = useState<boolean>(false);

    const handleNumClick = (num: string) => {
        if (waitingForNewInput) {
            setInput(num);
            setWaitingForNewInput(false);
        } else {
            setInput(input === '0' ? num : input + num);
        }
    };

    const clear = () => {
        setInput('0');
        setPreviousVal(null);
        setOperation(null);
        setWaitingForNewInput(false);
    };

    const handleOperation = (op: Operation) => {
        if (operation && !waitingForNewInput) {
            calculate();
        }
        setPreviousVal(parseFloat(input));
        setOperation(op);
        setWaitingForNewInput(true);
    };

    const calculate = () => {
        if (previousVal === null || operation === null) return;
        const current = parseFloat(input);
        let result = 0;

        switch (operation) {
            case '+': result = previousVal + current; break;
            case '-': result = previousVal - current; break;
            case '*': result = previousVal * current; break;
            case '/':
                if (current === 0) {
                    setInput('Error');
                    setPreviousVal(null);
                    setOperation(null);
                    return;
                }
                result = previousVal / current;
                break;
            case '^': result = Math.pow(previousVal, current); break;
        }

        const resultStr = String(Math.round(result * 10000000000) / 10000000000);
        setInput(resultStr);
        setPreviousVal(null);
        setOperation(null);
        setWaitingForNewInput(true);
    };

    const handleScientific = (func: string) => {
        const current = parseFloat(input);
        let result = 0;
        switch (func) {
            case 'sqrt':
                if (current < 0) {
                    setInput('Error');
                    setWaitingForNewInput(true);
                    return;
                }
                result = Math.sqrt(current);
                break;
            case 'log':
                if (current <= 0) {
                    setInput('Error');
                    setWaitingForNewInput(true);
                    return;
                }
                result = Math.log(current);
                break;
            case 'sin': result = Math.sin(current * (Math.PI / 180)); break;
            case 'cos': result = Math.cos(current * (Math.PI / 180)); break;
            case 'tan': result = Math.tan(current * (Math.PI / 180)); break;
        }
        const resultStr = String(Math.round(result * 10000000000) / 10000000000);
        setInput(resultStr);
        setWaitingForNewInput(true);
    }

    return (
        <div className="bg-white/30 dark:bg-white/5 backdrop-blur-xl border border-white/40 dark:border-white/10 p-6 rounded-3xl shadow-2xl w-full max-w-md transition-colors duration-500">
            {/* Display */}
            <div className="mb-6 p-4 bg-white/50 dark:bg-black/20 rounded-2xl text-right shadow-inner transition-colors duration-500">
                <div className="text-gray-600 dark:text-gray-400 text-sm h-6 font-medium">{operation ? `${previousVal} ${operation}` : ''}</div>
                <div className="text-5xl font-light text-slate-800 dark:text-white overflow-hidden whitespace-nowrap tracking-tight">{input}</div>
            </div>

            {/* Basic Grid */}
            <div className="grid grid-cols-4 gap-3">
                {/* Scientific Row 1 */}
                <button onClick={() => handleScientific('sin')} className="btn-scientific">sin</button>
                <button onClick={() => handleScientific('cos')} className="btn-scientific">cos</button>
                <button onClick={() => handleScientific('tan')} className="btn-scientific">tan</button>
                <button onClick={() => handleScientific('log')} className="btn-scientific">ln</button>

                {/* Scientific Row 2 */}
                <button onClick={() => handleScientific('sqrt')} className="btn-scientific">√</button>
                <button onClick={() => handleOperation('^')} className="btn-scientific">x^y</button>
                <button onClick={clear} className="col-span-2 btn-action bg-rose-500/90 hover:bg-rose-600 shadow-rose-500/30">AC</button>

                <button onClick={() => handleNumClick('7')} className="btn-num">7</button>
                <button onClick={() => handleNumClick('8')} className="btn-num">8</button>
                <button onClick={() => handleNumClick('9')} className="btn-num">9</button>
                <button onClick={() => handleOperation('/')} className="btn-op">÷</button>

                <button onClick={() => handleNumClick('4')} className="btn-num">4</button>
                <button onClick={() => handleNumClick('5')} className="btn-num">5</button>
                <button onClick={() => handleNumClick('6')} className="btn-num">6</button>
                <button onClick={() => handleOperation('*')} className="btn-op">×</button>

                <button onClick={() => handleNumClick('1')} className="btn-num">1</button>
                <button onClick={() => handleNumClick('2')} className="btn-num">2</button>
                <button onClick={() => handleNumClick('3')} className="btn-num">3</button>
                <button onClick={() => handleOperation('-')} className="btn-op">-</button>

                <button onClick={() => handleNumClick('0')} className="col-span-2 btn-num">0</button>
                <button onClick={() => handleNumClick('.')} className="btn-num">.</button>
                <button onClick={() => handleOperation('+')} className="btn-op">+</button>

                <button onClick={calculate} className="col-span-4 btn-action bg-blue-600/90 hover:bg-blue-700 shadow-blue-500/30 mt-2 text-2xl pb-1">=</button>
            </div>
        </div>
    );
};

export default Calculator;
