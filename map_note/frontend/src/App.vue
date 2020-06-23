<template>
  <div id="app">
    <div id = "map"></div>

    {{msg}}
    <form @submit.prevent="submitNote">
      <label>메모</label>
      <input type="text" v-model="formData.title"/>
      <br/>
      <button type="submit">Submit</button>
    </form>

    <br/>
    <h1>All notes</h1>
    <ul>
      <li v-for="(note, index) in notes" :key="index">
        <h3>{{note.title}}</h3>
        <h5>Created on {{note.created}}</h5>
        <p>{{note.content}}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import api from './api/index'
export default {
  name: 'app',
  data () {
    return {
      msg: '',
      formData: {
        title: '',
        content: ''
      },
      notes: []
    }
  },
  methods: {
    initMap() {
      var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };
var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
// 지도를 클릭했을때 클릭한 위치에 마커를 추가하도록 지도에 클릭이벤트를 등록합니다



      // 마커를 중앙에 생성합니다, 마커가 중복되서 찍히지 않기 위해 addmarker 함수밖으로 뺴줍니다.
      var marker = new kakao.maps.Marker({
          position: map.getCenter()
      });
      // 마커가 지도 위에 표시되도록 설정합니다
      marker.setMap(map);


kakao.maps.event.addListener(map, 'click', function(mouseEvent) {
    // 클릭한 위치에 마커를 표시합니다
    addMarker(mouseEvent.latLng);
});
// 지도에 표시된 마커 객체를 가지고 있을 배열입니다


var markers = [];
// 마커 하나를 지도위에 표시합니다
//addMarker(new kakao.maps.LatLng(33.450701, 126.570667));
// 마커를 생성하고 지도위에 표시하는 함수입니다
function addMarker(position) {

    //마커에 포지션을 바꿔주어 중복된 핑이 생기지 않게 해주는 함수입니다.
    marker.setPosition(position);

    // 생성된 마커를 배열에 추가합니다
    markers.push(marker);
}





// 배열에 추가된 마커들을 지도에 표시하거나 삭제하는 함수입니다
function setMarkers(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}
// "마커 보이기" 버튼을 클릭하면 호출되어 배열에 추가된 마커를 지도에 표시하는 함수입니다
function showMarkers() {
    setMarkers(map)
}
// "마커 감추기" 버튼을 클릭하면 호출되어 배열에 추가된 마커를 지도에서 삭제하는 함수입니다
function hideMarkers() {
    setMarkers(null);
}
        },
    submitNote () {
      api.fetchNotes('post', null, this.formData).then(res => {
        this.msg = 'Saved'
      }).catch((e) => {
        this.msg = e.response
      })
    },
    fetchAllNotes () {
      api.fetchNotes('get', null, null).then(res => {
        this.notes = res.data
        // check log data
        console.log(this.notes)
      }).catch((e) => {
        console.log(e)
      })
    }
  },
    mounted() {
      const script = document.createElement('script');
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = 'http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=9e9c50ee07c661cd80d3e59130f4703a';
      document.head.appendChild(script);
      this.fetchAllNotes()
    }
}
</script>
<style>
#map {
  text-align: center;
  width: 600px;
  height: 500px;
}
</style>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  max-width: 500px;
  margin: 0 auto;
  text-align: left;
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
  input, textarea{
    width: 100%;
    display: block;
    padding: 6px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  label{
    margin-top: 15px;
  }
  button{
    background: #000;
    color: #fff;
    border-radius: 3px;
    padding: 6px 10px;
  }
</style>
