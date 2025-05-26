document.addEventListener("SOMContentLoaded", () => {
	const feed = document.getElementById("feed")

	const updateFeed = (payload) => {
		const li = document.createElement("li")
		li.innerHTML = `${JSON.stringify(payload, null, 2)}`
		feed.appendChild(li)
	}

	const evtSource = new EventSource("/events")

	evtSource.onmessage = (msg) => {
		const data = JSON.parse(msg.data)
		updateFeed(data.payload)
	}
})
