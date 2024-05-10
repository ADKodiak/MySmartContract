pragma solidity ^0.8.1;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, Ownable {
    mapping(address => bool) private _whitelist;
    struct Proposal {
        uint256 id;
        address proposer;
        uint256 amount;
        address target;
        bool executed;
        uint256 endTime;
        uint256 votesFor;
        uint256 votesAgainst;
        bool isMint; // true pour mint, false pour burn
    }
    uint256 public nextProposalId;
    mapping(uint256 => Proposal) public proposals;
    uint256 public voteDuration = 2 minutes;  // Durée du vote

    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
        addToWhitelist(msg.sender);
    }

    modifier onlyWhitelisted() {
        require(_whitelist[msg.sender], "Vous n'etes pas autorise.");
        _;
    }

    function addToWhitelist(address account) public onlyOwner {
        _whitelist[account] = true;
    }

    function removeFromWhitelist(address account) public onlyOwner {
        _whitelist[account] = false;
    }

    function createProposal(uint256 amount, address target, bool isMint) public onlyOwner {
        proposals[nextProposalId] = Proposal(
            nextProposalId,
            msg.sender,
            amount,
            target,
            false,
            block.timestamp + voteDuration,
            0,
            0,
            isMint
        );
        nextProposalId++;
    }

    function vote(uint256 proposalId, bool support) public {
        require(balanceOf(msg.sender) > 0, "Vous devez posseder des tokens pour voter.");
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp < proposal.endTime, "Le temps de vote est ecoule.");
        
        if (support) {
            proposal.votesFor += balanceOf(msg.sender);
        } else {
            proposal.votesAgainst += balanceOf(msg.sender);
        }
    }

    function executeProposal(uint256 proposalId) public {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.endTime, "Le vote n'est pas encore fini.");
        require(!proposal.executed, "La proposition a deja ete executee.");
        
        uint256 totalVotes = proposal.votesFor + proposal.votesAgainst;
        if (proposal.votesAgainst <= proposal.votesFor || proposal.votesAgainst < totalVotes / 2) {
            if (proposal.isMint) {
                _mint(proposal.target, proposal.amount);
            } else {
                _burn(proposal.target, proposal.amount);
            }
            proposal.executed = true;
        }
    }

    function _transfer(address from, address to, uint256 amount) internal override onlyWhitelisted {
        require(_whitelist[to], "Destinataire non autorise.");
        super._transfer(from, to, amount);
    }
}
