//console.log("hello world")
const OpenAI =require('openai');
const apikey=""
const { configuration: OpenAIApi } = require("openai");
const express=require('express')
var cors=require('cors')
const app=express()


const openai = ({
    apiKey: "", // This is the default and can be omitted
  });

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a helpful assistant." }],
    model: "gpt-4o",
  });

  console.log(completion.choices[0]);
}

main();
