/*
 * The start page hero's little show: the template beside it renders in a tiny browser, and the line being
 * evaluated lights up. A name fills in, messages repeat in, one gets clicked (a component action, so the URL
 * turns into a /no/ URL) and its page opens, then it's back to the inbox for the next user.
 * Visitors who prefer reduced motion get the first inbox, fully rendered and still.
 */
(function () {
	const figure = document.querySelector(".hero-code");

	if (!figure) {
		return;
	}

	const pre = figure.querySelector("pre");
	const line = figure.querySelector(".hero-line");
	const url = figure.querySelector(".hero-output-url");
	const inbox = figure.querySelector('[data-page="inbox"]');
	const message = figure.querySelector('[data-page="message"]');
	const name = inbox.querySelector(".hero-output-name");
	const list = inbox.querySelector("ul");

	// Template lines, counted from 0
	const USER_NAME = 0, IF = 2, REPETITION = 4, LINK = 6, SUBJECT = 7;

	const USERS = [
		{ name: "Ada", messages: [
			{ subject: "Lunch on Friday?", text: "The ginger place, twelve-ish?" },
			{ subject: "Build #412 passed", text: "All green. Ship it." },
			{ subject: "Slides for November", text: "Draft attached. Thoughts welcome." }
		], open: 2 },
		{ name: "Linus", messages: [] },
		{ name: "Grace", messages: [
			{ subject: "Found a bug in the moth", text: "Literally. Taped it into the log." },
			{ subject: "Re: hot swapping", text: "Didn't even restart. Lovely." }
		], open: 1 }
	];

	const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
	const wait = ms => new Promise(resolve => setTimeout(resolve, ms));

	function highlight(n) {
		if (n === null) {
			line.classList.remove("on");
			return;
		}

		const style = getComputedStyle(pre);
		const height = parseFloat(style.lineHeight);
		line.style.top = (pre.offsetTop + parseFloat(style.paddingTop) + n * height) + "px";
		line.style.height = height + "px";
		line.classList.add("on");
	}

	function showPage(page) {
		inbox.hidden = page !== inbox;
		message.hidden = page !== message;
	}

	function item(subject) {
		const li = document.createElement("li");
		const a = document.createElement("span");
		a.className = "hero-output-link";
		a.textContent = subject;
		li.append(a);
		list.append(li);
		return li;
	}

	function reset() {
		showPage(inbox);
		url.textContent = "localhost:1200/inbox";
		name.textContent = "";
		list.replaceChildren();
		list.classList.remove("empty");
	}

	async function type(target, text) {
		for (const c of text) {
			target.textContent += c;
			await wait(70);
		}
	}

	async function render(user, step) {
		reset();
		await wait(500);

		highlight(USER_NAME);
		await wait(350);
		await type(name, user.name);
		await wait(700);

		highlight(IF);
		await wait(900);

		if (user.messages.length === 0) {
			list.classList.add("empty");
			highlight(null);
			await wait(2600);
			return;
		}

		const items = [];

		for (const m of user.messages) {
			highlight(REPETITION);
			await wait(450);
			highlight(SUBJECT);
			items.push(item(m.subject));
			await wait(550);
		}

		highlight(null);
		await wait(1200);

		const chosen = user.messages[user.open];
		const target = items[user.open].querySelector(".hero-output-link");
		highlight(LINK);
		target.classList.add("pressed");
		await wait(700);

		showPage(message);
		url.textContent = "localhost:1200/no/" + Math.random().toString(16).slice(2, 10) + "." + (step + 2);
		message.querySelector(".hero-output-subject").textContent = chosen.subject;
		message.querySelector(".hero-output-text").textContent = chosen.text;
		highlight(null);
		await wait(2800);
	}

	async function run() {
		for (let step = 0; ; step++) {
			// Rest while the tab is in the background
			while (document.hidden) {
				await wait(1000);
			}

			await render(USERS[step % USERS.length], step);
		}
	}

	if (reducedMotion) {
		name.textContent = USERS[0].name;
		USERS[0].messages.forEach(m => item(m.subject));
		return;
	}

	run();
})();
