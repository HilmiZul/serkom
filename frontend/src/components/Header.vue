<template>
  <div class="container">
    <div class="row mt-3 mb-3">
      <div class="col-md-2">
        <img src="/static/gambar/logo-smkn4.png" class="logo">
      </div>
      <div class="col-md-10">
        <div class=" mt-3">
          <h3><strong>{{ nama }}</strong> {{ judul }}</h3>
          <h5>{{ sub }}</h5>
          <p>{{ alamat }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      nama: 'e-Perpus',
      judul: 'SMK Negeri 4 Tasikmalaya',
      sub: 'Aplikasi Pencarian Buku',
      alamat: 'Jl.Depok, Sukamenak, Purbaratu'
    }
  }
}
</script>
