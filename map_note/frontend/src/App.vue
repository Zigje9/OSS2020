<template>
  <div id="app">
    <div style="width:600px; height:150px; border:1px solid #ff0000; float:left; margin-bottom:10px;">
      <p><big>사용 방법</big></p>
      <p>1. 메모를 남기고 싶은 장소를 클릭합니다.<br/>(클릭한 곳의 좌표가 지도밑에 보여집니다.)<br/>2. 메모를 작성합니다. <br/>3. summit을 눌러 저장합니다</p>
    </div>

    <div id="map"></div>

    <div id="minimap"></div>

<!--    현재 클릭된 위치의 좌표 정보를 보여줍니다.-->
    <div id="clickLatlng"></div>

    {{msg}}
    <form @submit.prevent="submitNote">
      <label>메모</label>
      <input type="text" v-model="formData.memo"/>
      <br/>
      <button type="submit">Submit</button>
    </form>

    <br/>
    <h1>메모 목록</h1>
    <ul>
      <li v-for="(note, index) in notes" :key="index">
        <h3>{{note.memo}}</h3>

        <h5>위도 :{{note.latitudes}}     경도 : {{note.longitudes}}</h5>
        <h6>Created on {{note.created}}</h6>
      </li>
    </ul>
  </div>
</template>

<script>
  let lat = 0;
  let lon = 0;
  import api from './api/index'

  export default {
    name: 'app',
    data() {
      return {
        msg: '',
        formData: {
          memo: '',
          latitudes: '',
          longitudes: '',
        },
        notes: []
      }
    },
    methods: {
      initMap() {
        var mapContainer = document.getElementById('map'), // 지도를 표시할 div
          mapOption = {
            center: new kakao.maps.LatLng(37.29544298322545, 126.83567569659414), // 지도의 중심좌표 한양대
            level: 3 // 지도의 확대 레벨
          };
         this.map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
        // ***** map 에서 this.map 으로 바꿔주면서 생성한 map을 모든함수에서 접근가능하게 만들어주었습니다.
        // 지도를 클릭했을때 클릭한 위치에 마커를 추가하도록 지도에 클릭이벤트를 등록합니다
        // 마커를 중앙에 생성합니다, 마커가 중복되서 찍히지 않기 위해 addmarker 함수밖으로 뺴줍니다.
        var marker = new kakao.maps.Marker();

        // 마커가 지도 위에 표시되도록 설정합니다
        marker.setMap(this.map);
        kakao.maps.event.addListener(this.map, 'click', function (mouseEvent) {
          var latlng = mouseEvent.latLng;
          lat = latlng.getLat();
          lon = latlng.getLng();

          // 클릭한 위치에 마커를 표시합니다
          addMarker(mouseEvent.latLng);


          //현재 클릭된 위치의 좌표 정보를 보여줍니다.
          var latlng = mouseEvent.latLng;//위치를 저장함
          var message = '현재 핑의 위치입니다.<br/> 위도 : ' + latlng.getLat() + '<br/>경도 : ' + latlng.getLng() + '<br/>--------------------------------------------<br/>';
          var resultDiv = document.getElementById('clickLatlng');
          resultDiv.innerHTML = message;


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
          setMarkers(this.map)
        }

        // "마커 감추기" 버튼을 클릭하면 호출되어 배열에 추가된 마커를 지도에서 삭제하는 함수입니다
        function hideMarkers() {
          setMarkers(null);
        }
        this.printdatamarker() //printdatamarker를 호출해줍니다.
      },

      submitNote() {
        //선택한 좌표를 저장
        this.formData.latitudes = lat;
        this.formData.longitudes = lon;
        //지역을 선택안하거나 메모를 입력이 안되있을 경우를 대비
        if (this.formData.latitudes == '0' || this.formData.longitudes == '0') {

          this.msg = '지역을 선택해주세요'

        } else if (this.formData.memo == '') {
          this.msg = '메모를 입력해주세요'

        } else {
          api.fetchNotes('post', null, this.formData).then(res => {
            location.reload();// 페이지 새로 고침
          }).catch((e) => {
            this.msg = e.response
          })
        }

      },
      fetchAllNotes() {
        api.fetchNotes('get', null, null).then(res => {
          this.notes = res.data
          // check log data
          console.log(this.notes)
        }).catch((e) => {
          console.log(e)
        })
      },
      printdatamarker() {   //데이터베이스에 있는 마커들을 지도 위에 출력해주는 함수입니다.
        api.fetchNotes('get', null, null).then(res => {
          this.notes = res.data

          let arrdatapositions = [];  //데이터베이스에서 받아오는 값들을 배열로 받았습니다.
          for (var i = 0; i < this.notes.length; i++) {
            arrdatapositions[i] = {
              title: this.notes[i].memo,
              latlng: new kakao.maps.LatLng(this.notes[i].latitudes, this.notes[i].longitudes)  //메모의 내용과 위도와 경도를 받아주는 과정입니다.
            }
          }

          var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
          //데이터 베이스에 있는 마커입니다. 현재 마커와 차이를 두기위해 다른 이미지를 선택했습니다.

          for (var i = 0; i < arrdatapositions.length; i++) {

            // 마커 이미지의 이미지 크기 입니다
            var imageSize = new kakao.maps.Size(24, 35);

            // 마커 이미지를 생성합니다
            var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

            // 마커를 생성합니다
            const marker = new kakao.maps.Marker({
              map: this.map, // 마커를 표시할 지도
              position: arrdatapositions[i].latlng, // 마커를 표시할 위치
              title: arrdatapositions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image: markerImage // 마커 이미지
            });
          }
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

  input, textarea {
    width: 100%;
    display: block;
    padding: 6px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  label {
    margin-top: 15px;
  }

  button {
    background: #000;
    color: #fff;
    border-radius: 3px;
    padding: 6px 10px;
  }
</style>

