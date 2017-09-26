<template>
  <div id="app">

    <div id="pew" style="height: 300px; background-color: #D3D6DB; flex-grow: 2; height: 100vh;">
      <div style="height: 60px; background-color: white; position: relative; top: 0; left: 0; width: 100%"></div>
      <div style="display: flex; flex-direction: column; justify-content:center; align-items:center; margin-top: 100px;">
      <canvas id="canvas"></canvas> 
      
      
      <div style="margin-top: 20px; color: #BE3144">
      <a @click="simulate" class="sim-button"><i class="fa fa-play-circle fa-3x" aria-hidden="true"></i></a>
      <a @click="stopSim" class="sim-button"><i class="fa fa-stop-circle fa-3x" aria-hidden="true"></i></a>
      </div>
      </div>
    </div>

    <div style="height: 300px; background-color: #303841; flex-grow: 2; height: 100vh;">

    </div>

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
      positions: [],
      timer: null
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
      this.canvas.width = 500
      this.canvas.height = 500
      this.canvas.style.width = `500px`
      this.canvas.style.height = `500px`
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

    simulate() {
      this.timer = window.setInterval(() => {
        this.genMatrix()
        this.render(this.positions)
      }, 1000);
    },

    stopSim() {
      window.clearInterval(this.timer);
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
body {
  margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: red;
  height: 100vh;
  display: flex;
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
  color: #BE3144;
}

.sim-button {
  margin: 0 10px 0 10px;
  cursor: pointer;
}

.sim-button:hover, .sim-button:active {
  color: #842d38;
}
</style>
