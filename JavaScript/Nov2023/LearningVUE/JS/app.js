const app = Vue.createApp({
    // you can add data, templates and methods here
    data() {
        return {
            title: "Hitchhiker's guide to the galaxy",
            author: "Douglas Adams",
            age: 42,
            // condition to show or hide books
            showBooks: true,
            x: 0,
            y: 0,
            // array of books with title and author
            books: [
                {title: 'Github', date: '10/22', img: 'Assets/Image1.png', isFav: true},
                {title: 'JavaScript', date: '12/22', img: 'Assets/Image2.png',  isFav: false},
                {title: 'VUE', date: '11/23',  img: 'Assets/Image3.png', isFav: true},               
            ],
            url: "https://github.com/Matthattan/Programming-Portfolio"
        }
    },
    // Function to change title on HTML
    methods: {
        changeColor() {
            this.style.color = "red"
        },
        // do the inverse of what the current state of showBooks is
        toggleShowBooks() {
            this.showBooks = !this.showBooks

        },
        // passing meteadata of event
        handleEvent(e, data) {
            console.log(e, e.type)
            if (data) {
                console.log(data)
            }
        },
        handleMouseMove(e) {
            this.x = e.offsetX
            this.y = e.offsetY
        },
        // change the state of isFav in order to change the dynamic background color
        favouriteItem(book) {
            book.isFav = !book.isFav
        }
    },
    computed: {
        filteredApps() {
            return this.books.filter((book) => book.isFav)
        }
    }
})

app.mount('#app')