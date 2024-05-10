# Voted ERC-20 Token Project on Sepolia Testnet 🚀

Welcome to the GitHub repository of our cutting-edge smart contract deployment for an ERC-20 token with advanced functionalities on the Sepolia Testnet! This project introduces a decentralized voting mechanism that empowers investors to decide on key token management features like minting and burning tokens.

## Features 🌟

- **ERC-20 Standard Compliance**: The token adheres to the popular ERC-20 standard, ensuring compatibility with a wide range of wallets and exchanges.
- **Whitelist System**: A robust whitelist system to control participation in certain token actions.
- **Admin Controls**: Administrators can mint or burn tokens based on the outcome of community votes.
- **Decentralized Voting**: Token holders can vote on proposals to enable or disable minting and burning functions, enhancing community involvement and decision-making.

## Project Structure 📂

- **deployERC-20.py**: Utilizes web3.py for deploying the smart contract. Ensure your private key and Infura project link are specified for node interaction.
- **votedToken.sol**: The Solidity source code for our smart contract implementing the token.
- **addWhiteList.py**: Executes transactions to add an address to the whitelist.
- **proposeVote.py**: Allows the administrator to propose a vote for minting or burning tokens.
- **vote.py**: Enables token holders to vote on active proposals.
- **executeVote.py**: Processes the outcome of a vote and executes the effects based on the decision once the voting period has ended.

## How to Use 🛠

1. **Set Up Environment**: Ensure you have Python and Node.js installed along with the necessary libraries and frameworks (e.g., web3.py, Solidity).
2. **Clone Repository**: `git clone https://github.com/yourgithub/repo.git`
3. **Configuration**: Create .env file with your private key and Infura API link.
4. **Deployment and Interaction**:
    - Run `python deployERC-20.py` to deploy the token.
    - Use the Python scripts provided to manage whitelist entries, propose and execute votes, and participate in token governance.

## Disclaimer ⚠️

**Important**: The smart contract code provided in this repository has **not** been audited and may contain security vulnerabilities. If you choose to use or interact with this code, you do so at your own risk. We strongly recommend reviewing and testing the code thoroughly before any live deployment or substantial investment.

## Contributing 👥

We encourage community contributions! Whether it's filing bugs, discussing improvements, or proposing new features, feel free to fork the repo, make your changes, and submit a pull request.

## License 📄

This project is released under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Support 💬

Need help? Open an issue for support or contact me.

Enjoy building and deploying your decentralized solutions with our Voted ERC-20 Token on Sepolia! 🌐✨
