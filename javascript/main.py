const Discord = require('discord.js');
const math = require('mathjs');
const express = require('express');
const { createCanvas, loadImage } = require('canvas');
const { registerFont } = require('canvas');
const canvas = createCanvas(500, 500);
const ctx = canvas.getContext('2d');
const app = express();

app.get('/', (req, res) => {
  res.send('[+] Ready');
});

function run() {
  app.listen(8000, '0.0.0.0');
}

function keep_alive() {
  const server = Thread(target=run);
  server.start();
}

const client = require('wolfram-alpha').createClient('wolfram_id');
const aeval = require('asteval').Interpreter;
const openai = require('openai');

const bot = new Discord.Client();
const status = ['!help', '!ask', '!ai'];
let statusIndex = 0;

bot.on('ready', () => {
  console.log('[+] Ready');
  setInterval(() => {
    bot.user.setActivity(status[statusIndex]);
    statusIndex = (statusIndex + 1) % status.length;
  }, 10000);
});

bot.on('message', async (message) => {
  if (message.content.startsWith('!flag')) {
    message.channel.send('intrepidbird{m47h3mag1c14n}');
  } else if (message.content.startsWith('!calculate')) {
    const expr = message.content.substring('!calculate'.length).trim();
    try {
      const x = aeval(expr);
      message.channel.send(x);
    } catch {
      message.channel.send('Please enter a valid mathematical expression.');
    }
  } else if (message.content.startsWith('!graph')) {
    const expression = message.content.substring('!graph'.length).trim();
    const x_vals = math.range(-10, 10, 0.01).toArray();
    const y_vals = x_vals.map((x) => math.evaluate(expression, { x }));
    const width = 800;
    const height = 600;
    const padding = 40;

    const canvas = createCanvas(width, height);
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, width, height);

    ctx.strokeStyle = 'black';
    ctx.lineWidth = 2;

    ctx.beginPath();
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height - padding);
    ctx.lineTo(width - padding, height - padding);
    ctx.stroke();

    ctx.font = '12px Arial';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    const xScale = (width - 2 * padding) / (x_vals[x_vals.length - 1] - x_vals[0]);
    const yScale = (height - 2 * padding) / (math.max(...y_vals) - math.min(...y_vals));

    for (let i = 0; i < x_vals.length; i++) {
      const x = padding + (x_vals[i] - x_vals[0]) * xScale;
      const y = height - padding - (y_vals[i] - math.min(...y_vals)) * yScale;

      ctx.beginPath();
      ctx.arc(x, y, 2, 0, 2 * Math.PI);
      ctx.fill();

      if (i > 0) {
        const prevX = padding + (x_vals[i - 1] - x_vals[0]) * xScale;
        const prevY = height - padding - (y_vals[i - 1] - math.min(...y_vals)) * yScale;

        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(x, y);
        ctx.stroke();
      }

      if (i % 10 === 0) {
        ctx.fillText(x_vals[i].toFixed(2), x, height - padding / 2);
      }
    }

    const buffer = canvas.toBuffer('image/png');
    message.channel.send({ files: [buffer] });
  } else if (message.content.startsWith('!factorial')) {
    const number = parseInt(message.content.substring('!factorial'.length).trim());
    const result = math.factorial(number);
    if (result.toString().length > 2000) {
      const fs = require('fs');
      fs.writeFileSync('factorial_result.txt', `The factorial of ${number} is: ${result}`);
      message.channel.send('The result is over 2000 digits. It has been written to "factorial_result.txt".', {
        files: ['factorial_result.txt'],
      });
      fs.unlinkSync('factorial_result.txt');
    } else {
      message.channel.send(`The factorial of ${number} is: ${result}`);
    }
  } else if (message.content.startsWith('!square')) {
    const number = parseFloat(message.content.substring('!square'.length).trim());
    const result = number ** 2;
    message.channel.send(`The square of ${number} is: ${result}`);
  } else if (message.content.startsWith('!factor')) {
    const number = parseInt(message.content.substring('!factor'.length).trim());
    const factors = [];
    for (let i = 1; i <= number; i++) {
      if (number % i === 0) {
        factors.push(i);
      }
    }
    message.channel.send(`The factors of ${number} are: ${factors}`);
  } else if (message.content.startsWith('!sqrt')) {
    const number = parseFloat(message.content.substring('!sqrt'.length).trim());
    if (number < 0) {
      message.channel.send('Cannot calculate the square root of a negative number');
    } else {
      const result = math.sqrt(number);
      message.channel.send(`The square root of ${number} is: ${result}`);
    }
  } else if (message.content.startsWith('!log')) {
    const args = message.content.substring('!log'.length).trim().split(' ');
    const number = parseFloat(args[0]);
    const base = parseFloat(args[1]);
    if (number <= 0 || base <= 0) {
      message.channel.send('Cannot calculate the logarithm of a non-positive number or with a non-positive base');
    } else {
      const result = math.log(number, base);
      message.channel.send(`The logarithm base ${base} of ${number} is: ${result}`);
    }
  } else if (message.content.startsWith('!cube')) {
    const number = parseFloat(message.content.substring('!cube'.length).trim());
    const result = number ** 3;
    message.channel.send(`The cube of ${number} is: ${result}`);
  } else if (message.content.startsWith('!sin')) {
    const number = parseFloat(message.content.substring('!sin'.length).trim());
    const result = math.sin(math.unit(number, 'deg'));
    message.channel.send(`The sine of ${number} is: ${result}`);
  } else if (message.content.startsWith('!cos')) {
    const number = parseFloat(message.content.substring('!cos'.length).trim());
    const result = math.cos(math.unit(number, 'deg'));
    message.channel.send(`The cosine of ${number} is: ${result}`);
  }
});

bot.login('your_token');

async function cos(ctx, number) {
    const result = Math.cos(Math.radians(number));
    await ctx.send(`The cosine of ${number} is: ${result}`);
}

bot.command('tan', async function(ctx, number) {
    const result = Math.tan(Math.radians(number));
    await ctx.send(`The tangent of ${number} is: ${result}`);
});

bot.command('ln', async function(ctx, number) {
    if (number <= 0) {
        await ctx.send("Cannot calculate the natural logarithm of a non-positive number");
    } else {
        const result = Math.log(number);
        await ctx.send(`The natural logarithm of ${number} is: ${result}`);
    }
});

bot.command('exp', async function(ctx, number) {
    const result = Math.exp(number);
    await ctx.send(`The exponential of ${number} is: ${result}`);
});

bot.command('is_prime', async function(ctx, number) {
    if (number <= 1) {
        await ctx.send(`${number} is not a prime number.`);
    } else if (number === 2) {
        await ctx.send(`${number} is a prime number.`);
    } else {
        for (let i = 2; i < number; i++) {
            if (number % i === 0) {
                await ctx.send(`${number} is not a prime number.`);
                break;
            }
        }
        await ctx.send(`${number} is a prime number.`);
    }
});

bot.command('abs', async function(ctx, number) {
    const result = Math.abs(number);
    await ctx.send(`The absolute value of ${number} is: ${result}`);
});

bot.command('pow', async function(ctx, base, exponent) {
    const result = Math.pow(base, exponent);
    await ctx.send(`${base} raised to the power of ${exponent} is: ${result}`);
});

bot.command('mod', async function(ctx, number1, number2) {
    const result = number1 % number2;
    await ctx.send(`The remainder of the division of ${number1} by ${number2} is: ${result}`);
});

bot.command('hypot', async function(ctx, side1, side2) {
    const result = Math.hypot(side1, side2);
    await ctx.send(`The length of the hypotenuse for a right triangle with sides ${side1} and ${side2} is: ${result}`);
});

bot.command('solve_quad', async function(ctx, a, b, c) {
    const d = (b**2) - (4*a*c);
    const sol1 = (-b-cmath.sqrt(d))/(2*a);
    const sol2 = (-b+cmath.sqrt(d))/(2*a);
    await ctx.send(`The solutions are ${sol1} and ${sol2}`);
});

bot.command('std_dev', async function(ctx, ...args) {
    const data = args;
    const result = statistics.stdev(data);
    await ctx.send(`The standard deviation is ${result}`);
});

bot.command('fibonacci', async function(ctx, n) {
    let a = 0, b = 1;
    const fib_sequence = [];
    while (a < n) {
        fib_sequence.push(a);
        [a, b] = [b, a+b];
    }
    await ctx.send(`The Fibonacci sequence up to ${n} is: ${fib_sequence}`);
});

bot.command('inverse_matrix', async function(ctx, ...args) {
    const matrix = np.array(args).reshape((int(np.sqrt(len(args)))), -1);
    try {
        const inverse = np.linalg.inv(matrix);
        await ctx.send(`The inverse of the matrix is: ${inverse}`);
    } catch (error) {
        await ctx.send("The matrix is not invertible.");
    }
});

bot.command('goat', async function(ctx) {
    await ctx.send("Gauss is the Greatest of all Time in Mathematics");
});

bot.command('determinant', ...);

async function determinant(ctx, ...args) {
    const matrix = new Array(args.length).fill(0).map((_, i) => args[i]);
    const size = Math.sqrt(args.length);
    const reshapedMatrix = [];
    for (let i = 0; i < size; i++) {
        reshapedMatrix.push(matrix.slice(i * size, (i + 1) * size));
    }
    const det = math.det(reshapedMatrix);
    await ctx.send(`The determinant of the matrix is: ${det}`);
}

bot.command('ask', async function (ctx, question) {
    try {
        const res = await client.query(question);
        if (res['@success'] === 'false') {
            await ctx.send('I could not find an answer to your question.');
        } else {
            const answer = res.results[0].text;
            await ctx.send(`The answer to your question is: ${answer}`);
        }
    } catch (e) {
        await ctx.send(`An error occurred ${e}`);
    }
});

bot.command('solve', async function (ctx, a, b, c) {
    const d = (b ** 2) - (4 * a * c);
    const sol1 = (-b - Math.sqrt(d)) / (2 * a);
    const sol2 = (-b + Math.sqrt(d)) / (2 * a);
    await ctx.send(`The solutions are ${sol1} and ${sol2}`);
});

bot.command('eigen', async function (ctx, ...args) {
    const matrix = new Array(args.length).fill(0).map((_, i) => args[i]);
    const size = Math.sqrt(args.length);
    const reshapedMatrix = [];
    for (let i = 0; i < size; i++) {
        reshapedMatrix.push(matrix.slice(i * size, (i + 1) * size));
    }
    try {
        const { eigenvalues, eigenvectors } = math.eigs(reshapedMatrix);
        await ctx.send(`The eigenvalues of the matrix are: ${eigenvalues}, and the corresponding eigenvectors are: ${eigenvectors}`);
    } catch (error) {
        await ctx.send("The eigenvalues and eigenvectors could not be calculated.");
    }
});

bot.command('ai', async function (ctx, prompt) {
    openai.api_key = 'openai_key';
    const response = await openai.Completion.create({ engine: "text-davinci-002", prompt: prompt, max_tokens: 100 });
    await ctx.send(response.choices[0].text.trim());
});

bot.command('three_d', async function (ctx) {
    // Your code for the 'three_d' command goes here
});

async function three_d(ctx) {
    await ctx.send("https://www.desmos.com/3d");
}

bot.run('token');
