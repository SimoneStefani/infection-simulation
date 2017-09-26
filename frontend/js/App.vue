<template>
  <div id="app">
    <canvas id="canvas"></canvas>
  </div>
</template>

<script>
export default {
  name: 'app',

  data () {
    return {
      canvas: null,
      context: null,
      scale: 10,
      interval: 100,
      positions: []
    }
  },
  
  mounted () {
    this.setupCanvas()
    this.genMatrix()
    this.render(this.positions)
  },

  methods: {
    setupCanvas () {
      this.canvas = document.getElementById("canvas")
      this.context = this.canvas.getContext("2d")
      let ratio = this.getPixelRatio(this.context)
      this.canvas.width = document.getElementById("app").clientWidth * ratio
      this.canvas.height = (document.getElementById("app").clientWidth - 120) * ratio
      this.canvas.style.width = `${document.getElementById("app").clientWidth}px`
      this.canvas.style.height = `${document.getElementById("app").clientWidth - 120}px`
      this.context.scale(ratio, ratio)
      this.context.fillStyle = 'rgb(111, 168, 220)'
    },

    getPixelRatio (context) {
      var backingStore = context.backingStorePixelRatio ||
              context.webkitBackingStorePixelRatio ||
              context.mozBackingStorePixelRatio ||
              context.msBackingStorePixelRatio ||
              context.oBackingStorePixelRatio ||
              context.backingStorePixelRatio || 1
      return (window.devicePixelRatio || 1) / backingStore
    },

    render (positions) {
      this.context.clearRect(0, 0, this.canvas.width, this.canvas.height)
      positions.forEach(({x, y, n}) => {
          this.context.fillRect(x * this.scale, y * this.scale, this.scale, this.scale)
          if (n == 0) {
            this.context.fillStyle = 'rgb(32, 80, 129)'
          } else if (n == 1) {
            this.context.fillStyle = 'rgb(255, 217, 102)'
          } else if (n == 2) {
            this.context.fillStyle = 'rgb(218, 89, 97)'
          } else {
            this.context.fillStyle = 'rgb(111, 168, 220)'
          }
      })      
    },

    genMatrix() {
      for (var i = 0; i < 50; i++) {
        for (var j = 0; j < 50; j++) {
          let num = this.getRandomInt(0, 2);
          this.positions.push({x: j, y: i, n: num})
        }
      }
    },

    getRandomInt(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
