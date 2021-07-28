<template>
  <div class="home">
    <div class="graph" id="vtuber-graph"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
export default {
  name: "Home",
  components: {},
  data(){
    return{
      nodeData:[],
      edgeData:[]
    }
  },
  methods: {
    graphInit() {
      let myChart = echarts.init(document.getElementById("vtuber-graph"));
      var option = {
        title: { text: "vtuber fans relation graph" },
        tooltip: {
          formatter: function (x) {
            return x.data.des;
          },
        },
        series: [
          {
            type: "graph",
            layout: "force",
            roam: true,
            zoom:1,
            focusNodeAdjacency: true,
            edgeSymbol: ["none", "none"],
            edgeSymbolSize: [4, 10],
            force: {
              repulsion: 3000,
              edgeLength: [500, 2000],
              gravity:0.05
            },
            draggable: true,
            itemStyle: {
              normal: {
                color: "#4b565b",
              },
            },
            // lineStyle: {
            //   normal: {
            //     width: 0.5,
            //     color: "#000000",
            //   },
            // },
            edgeLabel: {
              normal: {
                show: false,
                formatter: function (x) {
                  return x.data.name;
                },
              },
            },
            label: {
              normal: {
                show: true,
                textStyle: {},
              },
            },
            data: this.nodeData,
            links:this.edgeData
          },
        ],
      };
      myChart.setOption(option);
      myChart.on('click',(params)=>{
        if(params.dataType==='node'){
          let detailRoute = this.$router.resolve({path: "/detail",query:{uid: params.data.uid}})
          window.open(detailRoute.href)
          console.log(params)
        }
      })
    },
    getNodes(){
      this.$axios.post("api/getNodes",{}).then(res=>{
          this.nodeData = res.data
          this.getEdges()
        })
    },
    getEdges(){
      this.$axios.post("api/getEdges",{}).then(res=>{
          this.edgeData = res.data
          console.log(this.edgeData)
          this.graphInit()
        })
    }
  },
  mounted() {
    this.getNodes(); //链式调用。。。确保异步拉取数据也能顺序执行
  },
};
</script>

<style scoped>
.home,
.graph {
  height: 100%;
  width: 100%;
}
</style>
