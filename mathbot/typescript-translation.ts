import * as discord from 'discord.js';
import { Intents } from 'discord.js';
import { commands, tasks } from 'discord.js';
import * as math from 'mathjs';
import { cycle } from 'itertools';
import { Thread } from 'threading';
import * as plt from 'matplotlib.pyplot';
import * as np from 'numpy';
import * as flask from 'flask';
import * as cmath from 'cmath';
import * as statistics from 'statistics';
import * as np from 'numpy';
import { Interpreter } from 'asteval';
import * as wolframalpha from 'wolframalpha';
import * as cmath from 'cmath';
import { symbols, lambdify } from 'sympy';
import { parse_expr } from 'sympy.parsing.sympy_parser';
import * as openai from 'openai';

const client = wolframalpha.Client('wolfram_id');
const aeval = new Interpreter();
const app = flask.Flask('');

@app.route('/')

// 'Keep Alive' Stuff
function main() { return "[+] Ready"; }

function run() { app.run(host="0.0.0.0", port=8000); }

function keep_alive() {
const server = new Thread(run);
server.start();
}

const intents = new Intents();
intents.messages = true;
const bot = new commands.Bot({ commandPrefix: '!', intents: intents });
const status = cycle(['!help, !ask, !ai']);

bot.on('ready', () => {
change_status.start();
console.log("[+] Ready");
});

const change_status = new tasks.Loop(() => {
bot.user.setActivity(discord.Game(next(status)));
}, 10000);

// Commands

bot.command('flag', (ctx) => {
ctx.send("intrepidbird{m47h3mag1c14n}");
});

bot.command('calculate', (ctx, expr) => {
try {
const x = aeval(expr);
ctx.send(x);
} catch {
ctx.send('Please enter a valid mathematical expression.');
}
});

bot.command('graph', (ctx, expression) => {
const x = symbols('x');
const y_expr = parse_expr(expression);
const y_func = lambdify(x, y_expr, "numpy");

const x_vals = np.linspace(-10, 10, 1000);
const y_vals = y_func(x_vals);

plt.plot(x_vals, y_vals);
plt.savefig('graph.png');
ctx.send({ files: ['graph.png'] });
});

bot.command('factorial', (ctx, number) => {
const result = math.factorial(number);
if (result.toString().length > 2000) {
with open('factorial_result.txt', 'w') as f:
f.write(`The factorial of ${number} is: ${result}`);
ctx.send("The result is over 2000 digits. It has been written to 'factorial_result.txt'.");
ctx.send({ files: ['factorial_result.txt'] });
os.remove('factorial_result.txt'); // remove the file after sending it
} else {
ctx.send(`The factorial of ${number} is: ${result}`);
}
});

bot.command('square', (ctx, number) => {
const result = number ** 2;
ctx.send(`The square of ${number} is: ${result}`);
});

bot.command('factor', (ctx, number) => {
const factors = new Set();
for (let i = 1; i <= math.sqrt(number); i++) {
if (number % i === 0) {
factors.add(i);
factors.add(number/i);
}
}
ctx.send(`The factors of ${number} are: ${Array.from(factors)}`);
});

bot.command('sqrt', (ctx, number) => {
if (number < 0) {
ctx.send("Cannot calculate the square root of a negative number");
} else {
const result = math.sqrt(number);
ctx.send(`The square root of ${number} is: ${result}`);
}
});

bot.command('log', (ctx, number, base) => {
if (number <= 0 || base <= 0) {
ctx.send("Cannot calculate the logarithm of a non-positive number or with a non-positive base");
} else {
const result = math.log(number, base);
ctx.send(`The logarithm base ${base} of ${number} is: ${result}`);
}
});

bot.command('cube', (ctx, number) => {
const result = number ** 3;
ctx.send(`The cube of ${number} is: ${result}`);
});

bot.command('sin', (ctx, number) => {
const result = math.sin(math.radians(number));
ctx.send(`The sine of ${number} is: ${result}`);
});

bot.command('cos', (ctx, number) => {
const result = math.cos(math.radians(number));
ctx.send(`The cosine of ${number} is: ${result}`);
});

client.login('your-token-goes-here');
