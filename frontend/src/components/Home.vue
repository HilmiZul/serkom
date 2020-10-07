<template>
  <div class="hello">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="form-group">
            <input v-model="cari" type="search" class="form-control" placeholder="Coba cari: Pemrograman">
          </div>
          <table class="table table-bordered table-striped table-hover">
            <thead>
              <tr>
                <th>NO.</th>
                <th>COVER</th>
                <th>JUDUL</th>
                <th>PENULIS</th>
                <th>KELOMPOK</th>
                <th>JUMLAH</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(buku, i) in cariBuku" :key="buku.id">
                <td>{{ i+1 }}.</td>
                <td><img :src="buku.cover" class="cover"></td>
                <td>{{ buku.judul }}</td>
                <td>{{ buku.penulis }}</td>
                <td>{{ buku.kelompok }}</td>
                <td>{{ buku.jumlah }}</td>
              </tr>
            </tbody>
          </table>
          <p>{{ cariBuku.length }} item dari {{ total }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      books: [],
      cari: '',
      total: ''
    }
  },

  mounted () {
    fetch('http://127.0.0.1:8000/api/buku')
      .then(result => result.json())
      .then(data => {
        this.books = data
        this.total = data.length
      })
  },

  computed: {
    cariBuku () {
      return this.books.filter(b => {
        return (
          b.judul.toLowerCase().includes(this.cari.toLowerCase()) ||
          b.penulis.toLowerCase().includes(this.cari.toLowerCase()) ||
          b.kelompok.toLowerCase().includes(this.cari.toLowerCase())
        )
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cover {
  width: 70px;
}
</style>
