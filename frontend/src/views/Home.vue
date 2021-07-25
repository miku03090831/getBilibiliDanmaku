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
            edgeSymbol: ["circle", "arrow"],
            edgeSymbolSize: [4, 10],
            force: {
              repulsion: 2500,
              edgeLength: [80, 1000],
            },
            draggable: true,
            itemStyle: {
              normal: {
                color: "#4b565b",
              },
            },
            lineStyle: {
              normal: {
                width: 2,
                color: "#4b565b",
              },
            },
            edgeLabel: {
              normal: {
                show: true,
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
            data: [{
              name:"阿梓",
              uid:1234,
              symbolSize:Math.ceil(Math.log(12345))*10,
              des:"number of fan-club members: 1234"
            },{
              name:"七海",
              uid:12345,
              symbolSize:Math.ceil(Math.log(123456))*10,
              des:"number of fan-club members: 12345"
            },],
            links:[{
              source:"阿梓",
              target:"七海",
              des:"70%"
            }]
          },
        ],
      };
      myChart.setOption(option);
      myChart.on('click',(params)=>{
        if(params.dataType==='node'){
          let detailRoute = this.$router.resolve({path: "/detail",query:{name: params.data.name}})
          window.open(detailRoute.href)
          console.log(params)
        }
      })
    },
  },
  mounted() {
    
    this.graphInit();
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
