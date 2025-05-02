//evals.ts

import { EvalConfig } from 'mcp-evals';
import { openai } from "@ai-sdk/openai";
import { grade, EvalFunction } from "mcp-evals";

const run_codeEval: EvalFunction = {
    name: "run_codeEval",
    description: "Evaluates the ability to run Python code in a secure sandbox using Jupyter Notebook syntax",
    run: async () => {
        const result = await grade(openai("gpt-4"), "Please use the run_code tool to run the following Python code using Jupyter Notebook syntax: print('Hello from the sandbox!'). Return the output.");
        return JSON.parse(result);
    }
};

const config: EvalConfig = {
    model: openai("gpt-4"),
    evals: [run_codeEval]
};
  
export default config;
  
export const evals = [run_codeEval];