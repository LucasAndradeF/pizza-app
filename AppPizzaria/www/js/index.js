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
