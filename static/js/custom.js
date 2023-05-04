function getMinMaxFiltering(){
    let min_price = document.querySelector('.min_price').value;
    let max_price = document.querySelector('.max_price').value;
    filterProducts(min_price, max_price);
}

function filterProducts(min_price, max_price){
    let products = document.querySelectorAll('.product_item');
    products.forEach((product) => {
    product.style.display = 'block';
    let price = product.querySelector('.price').textContent.replace("$", "");
        if (Number(price) < Number(min_price) || Number(price) > Number(max_price)){
            product.style.display = 'none';
        }
    })
}

function addProduct(e){
    let product_radio1 = document.querySelectorAll('.product_radio1');
    let product_radio2 = document.querySelectorAll('.product_radio2');
    let color;
    let size;
    let product_id = e.getAttribute('data-product_id');

    product_radio1.forEach((item) => {
        let attr = item.classList
        if (attr.contains("active")){
            color = item.textContent.trim();
        }
    });

    product_radio2.forEach((item) => {
        let attr = item.classList
        if (attr.contains("active")){
            size = item.textContent.trim();
        }
    });

    ajaxAddProduct(color, size, product_id);
};


function ajaxAddProduct(color, size, product_id){
    $.ajax({
        url: '/store/ajaxAddProduct/',
        type: 'GET',
        data: { product_id: product_id, color: color, size: size },
        success: function(data){
            console.log(data)
        }
    });
}





