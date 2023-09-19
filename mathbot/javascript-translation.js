const Discord = require('discord.js');
const client = new Discord.Client();
const math = require('mathjs');
const { createCanvas, loadImage } = require('canvas');
const express = require('express');
const app = express();
const server = require('http').createServer(app);

app.get('/', (req, res) => res.send('[+] Ready'));
server.listen(8000, () => console.log('[+] Ready'));

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
    if (msg.content.startsWith('!calculate ')) {
        const expr = msg.content.substring(11);
        try {
            const result = math.evaluate(expr);
            msg.reply(result.toString());
        } catch (err) {
            msg.reply('Please enter a valid mathematical expression.');
        }
    } else if (msg.content.startsWith('!graph ')) {
        const expr = msg.content.substring(7);
        try {
            const canvas = createCanvas(500, 500);
            const ctx = canvas.getContext('2d');
            const xValues = math.range(-10, 10, 0.1).toArray();
            const yValues = xValues.map(x => math.evaluate(expr, { x: x }));
            ctx.beginPath();
            ctx.moveTo(xValues[0], yValues[0]);
            for (let i = 1; i < xValues.length; i++) {
                ctx.lineTo(xValues[i], yValues[i]);
            }
            ctx.stroke();
            msg.channel.send({ files: [{ attachment: canvas.toBuffer() }] });
        } catch (err) {
            msg.reply('Please enter a valid mathematical expression.');
        }
    } else if (msg.content.startsWith('!factorial ')) {
        const number = parseInt(msg.content.substring(11));
        const result = math.factorial(number);
        msg.reply(`The factorial of ${number} is: ${result}`);
    } else if (msg.content.startsWith('!square ')) {
        const number = parseFloat(msg.content.substring(8));
        const result = math.pow(number, 2);
        msg.reply(`The square of ${number} is: ${result}`);
    } else if (msg.content.startsWith('!factor ')) {
        const number = parseInt(msg.content.substring(8));
        const factors = math.divide(math.range(1, number + 1).toArray(), number).filter(n => n % 1 === 0);
        msg.reply(`The factors of ${number} are: ${factors}`);
    } else if (msg.content.startsWith('!sqrt ')) {
        const number = parseFloat(msg.content.substring(6));
        if (number < 0) {
            msg.reply('Cannot calculate the square root of a negative number');
        } else {
            const result = math.sqrt(number);
            msg.reply(`The square root of ${number} is: ${result}`);
        }
    } else if (msg.content.startsWith('!log ')) {
        const numbers = msg.content.substring(5).split(' ').map(parseFloat);
        if (numbers.some(n => n <= 0)) {
            msg.reply('Cannot calculate the logarithm of a non-positive number or with a non-positive base');
        } else {
            const result = math.log(numbers[0], numbers[1]);
            msg.reply(`The logarithm base ${numbers[1]} of ${numbers[0]} is: ${result}`);
        }
    } else if (msg.content.startsWith('!cube ')) {
        const number = parseFloat(msg.content.substring(6));
        const result = math.pow(number, 3);
        msg.reply(`The cube of ${number} is: ${result}`);
    } else if (msg.content.startsWith('!sin ')) {
        const number = parseFloat(msg.content.substring(5));
        const result = math.sin(math.unit(number, 'deg'));
        msg.reply(`The sine of ${number} is: ${result}`);
    }
});

client.login('token');

// Only HALF the code btw
// npm install discord.js mathjs canvas express
// Please note some functions are not available thx

