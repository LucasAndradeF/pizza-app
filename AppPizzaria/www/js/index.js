async function loginUsuario() {
  // Coleta os valores dos inputs
  const email = document.getElementById("username").value;
  const senha = document.getElementById("password").value;

  const dadosLogin = {
    email: email,
    senha: senha,
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dadosLogin),
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Login bem-sucedido:", data);
      window.location.href = "menu.html";
    } else {
      const errorData = await response.json();
      console.error("Erro de login:", errorData);
      alert("Erro de login: " + errorData.error);
    }
  } catch (error) {
    console.error("Erro na requisição:", error);
    alert("Erro de conexão com o servidor");
  }
}

async function cadastrarUsuario() {
  const nome = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const senha = document.getElementById("password").value;

  const dadosCadastro = {
    nome: nome,
    email: email,
    senha: senha,
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/cadastro", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dadosCadastro),
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Cadastro bem-sucedido:", data);
      alert("Cadastro realizado com sucesso!");
      window.location.href = "index.html";
    } else {
      const errorData = await response.json();
      console.error("Erro de Cadastro:", errorData);
      alert("Erro de cadastro: " + errorData.error);
    }
  } catch (error) {
    console.error("Erro na requisição:", error);
    alert("Erro de conexão com o servidor");
  }
}


async function buscarPizzas() {
    try {
      const response = await fetch("http://127.0.0.1:5000/pizzas");
      const pizzas = await response.json();
  
      const pizzaListElement = document.getElementById("pizza-list");
      pizzaListElement.innerHTML = "";
  
      pizzas.forEach((pizza) => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `
          <strong>${pizza.nome}</strong> - R$ ${pizza.preco.toFixed(2)} <br>
          <strong>Recheio:</strong> ${pizza.recheio}
        `;
        pizzaListElement.appendChild(listItem);
      });
    } catch (error) {
      console.error("Erro ao buscar pizzas:", error);
    }
  }
  
  async function buscarDoces() {
    try {
      const response = await fetch("http://127.0.0.1:5000/doces");
      const doces = await response.json();
  
      const doceListElement = document.getElementById("doces-list");
      doceListElement.innerHTML = "";
  
      doces.forEach((doce) => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `
          <strong>${doce.nome}</strong> - R$ ${doce.preco.toFixed(2)} <br>
        `;
        doceListElement.appendChild(listItem);
      });
    } catch (error) {
      console.error("Erro ao buscar doces:", error);
    }
  }
  
  async function buscarBebidas() {
    try {
      const response = await fetch("http://127.0.0.1:5000/bebidas");
      const bebidas = await response.json();
  
      const bebidaListElement = document.getElementById("bebidas-list");
      bebidaListElement.innerHTML = "";
  
      bebidas.forEach((bebida) => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `
          <strong>${bebida.nome}</strong> - R$ ${bebida.preco.toFixed(2)} <br>
        `;
        bebidaListElement.appendChild(listItem);
      });
    } catch (error) {
      console.error("Erro ao buscar bebidas:", error);
    }
  }
  
  function mostrarItens(item) {

    document.getElementById("pizza-list").style.display = "none";
    document.getElementById("bebidas-list").style.display = "none";
    document.getElementById("doces-list").style.display = "none";
  
    if (item === "pizzas") {
      document.getElementById("pizza-list").style.display = "block";
      buscarPizzas();
    } else if (item === "doces") {
      document.getElementById("doces-list").style.display = "block";
      buscarDoces();
    } else if (item === "bebidas") {
      document.getElementById("bebidas-list").style.display = "block";
      buscarBebidas();
    }
  }
  