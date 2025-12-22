<script>
  // Edit listing
  $(document).on("click", ".js-edit-listing", function () {
    // 1. Ambil data dari tombol yang diklik
    const id = $(this).data("id");
    const name = $(this).data("name");
    const seller = $(this).data("seller");
    const price = $(this).data("price");
    const status = $(this).data("status");
    const deskripsi = $(this).data("deskripsi");
    console.log(id, name, seller, price, status, deskripsi);


    // 2. Masukkan ke Input Form (agar bisa diedit & disubmit)
    $("#editListingIdHidden").val(id); // Masuk ke input hidden
    $("#editListingName").val(name);
    $("#editListingPrice").val(price);
    $("#editListingStatus").val(status);
    $("#editListingDeskripsi").val(deskripsi);

    // 3. Masukkan ke Teks Info (hanya baca)
    $("#editListingIdText").text(id);
    $("#editListingSellerText").text(seller);
  });    

  // Take down confirm
  $(document).on("click", ".js-takedown", function () {
    const id = $(this).data("id");
    const name = $(this).data("name");
    const seller = $(this).data("seller");
    console.log(id, name, seller);

    $("#tdId").text(id || "-");
    $("#tdName").text(name || "-");
    $("#tdSeller").text(seller || "-");

    // Update tombol konfirmasi take down dengan data yang sesuai
    $(".confirm-takedown").data("id", id);
  });

  // User detail
  $(document).on("click", ".js-user-detail", function () {
    $("#udRole").text($(this).data("role") || "-");
    $("#udName").text($(this).data("name") || "-");
    $("#udEmail").text($(this).data("email") || "-");
    $("#udStatus").text($(this).data("status") || "-");

    $("#udMetric1").text($(this).data("metric1") || "-");
    $("#udMetric2").text($(this).data("metric2") || "-");
    $("#udMetric3").text($(this).data("metric3") || "-");
  });


  // AJAX: ubah status publish/unpublish
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  const csrftoken = getCookie('csrftoken');

  // === LOGIKA AJAX ===
  $(document).on("click", ".js-status-ajax", function () {
      const btn = $(this); // Tombol yang diklik
      const id = btn.data("id");
      const targetStatus = btn.data("status");
      
      // 1. Ubah tombol jadi "Loading..." biar user tahu proses jalan
      const originalText = btn.text();
      btn.prop("disabled", true).text("Processing...");

      // 2. Kirim Request ke Server
      fetch("{% url 'update_status' %}", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrftoken
          },
          body: JSON.stringify({
              id_jasa: id,
              status: targetStatus
          })
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              // === SUKSES: UPDATE TAMPILAN ===
              
              // A. Update Badge Status (Warna & Teks)
              const badge = $("#badge-status-" + id);
              badge.text(data.new_status);
              
              // Reset kelas warna badge
              badge.removeClass("badge-published badge-unpublished badge-takedown");
              
              if (data.new_status === "Published") {
                  badge.addClass("badge-published");
              } else if (data.new_status === "Unpublished") {
                  badge.addClass("badge-unpublished");
              } else if (data.new_status === "Taken Down") {
                  badge.addClass("badge-takedown");
              }

              // B. Update Tombol (Tukar Warna & Fungsi)
              if (targetStatus === "Published") {
                  // Sekarang sudah Published, tombol harus jadi "Unpublish" (Kuning)
                  btn.removeClass("btn-success").addClass("btn-warning");
                  btn.text("Unpublish");
                  btn.data("status", "Unpublished"); // Update data-status untuk klik berikutnya
              } if (targetStatus === "Unpublished") {
                  // Sekarang sudah Unpublished, tombol harus jadi "Publish" (Hijau)
                  btn.removeClass("btn-warning").addClass("btn-success");
                  btn.text("Publish");
                  btn.data("status", "Published");
              } else if (targetStatus === "Taken Down") {
                  const actionsCell = $("#a ctions-cell-" + id);
                  // Tombol Take Down di-disable
                  btn.text("Taken Down");
                  btn.prop("disabled", true);
                  
                  // Juga update tombol menjadi unpublish
                  actionsCell.find(".js-status-ajax").removeClass("btn-success btn-warning").addClass("btn-warning").text("Unpublish").data("status", "Unpublished");
              }

              // Update di modal edit juga
              $(document).find(".js-edit-listing[data-id='" + id + "']").data("status", data.new_status);
              $(document).find(".js-takedown[data-id='" + id + "']").prop("disabled", data.new_status === "Taken Down");

          } else {
              alert("Gagal: " + data.message);
              btn.text(originalText); // Balikin teks tombol
          }
      })
      .catch(error => {
          console.error("Error:", error);
          alert("Terjadi kesalahan koneksi.");
          btn.text(originalText);
      })
      .finally(() => {
          btn.prop("disabled", false); // Aktifkan tombol lagi
      });
  });
</script>
